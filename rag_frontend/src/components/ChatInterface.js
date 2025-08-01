import React, { useState, useRef, useEffect } from 'react';
import { Send, Image, X, Trash2 } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import './ChatInterface.css';

const ChatInterface = () => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [selectedImage, setSelectedImage] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const fileInputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleImageSelect = (event) => {
    const file = event.target.files[0];
    if (file && file.type.startsWith('image/')) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setSelectedImage({
          file: file,
          dataUrl: e.target.result,
          name: file.name
        });
      };
      reader.readAsDataURL(file);
    }
  };

  const removeSelectedImage = () => {
    setSelectedImage(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const clearChat = () => {
    if (messages.length === 0) return;
    
    if (window.confirm('Are you sure you want to clear all chat history? This action cannot be undone.')) {
      setMessages([]);
      setInputMessage('');
      setSelectedImage(null);
      if (fileInputRef.current) {
        fileInputRef.current.value = '';
      }
    }
  };

  const sendMessage = async () => {
    if (!inputMessage.trim() && !selectedImage) return;

    const userMessage = {
      role: 'user',
      content: inputMessage,
      timestamp: new Date(),
      image: selectedImage
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const requestBody = {
        message: inputMessage,
        conversation_history: messages.slice(-10), // Last 10 messages for context
        image_data: selectedImage ? selectedImage.dataUrl : null
      };

      const response = await fetch('/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      });

      const data = await response.json();

      if (response.ok) {
        const assistantMessage = {
          role: 'assistant',
          content: data.response,
          timestamp: new Date(),
          sources: data.sources || []
        };
        setMessages(prev => [...prev, assistantMessage]);
      } else {
        throw new Error(data.detail || 'Failed to get response');
      }
    } catch (error) {
      const errorMessage = {
        role: 'assistant',
        content: `Sorry, I encountered an error: ${error.message}`,
        timestamp: new Date(),
        isError: true
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
      setInputMessage('');
      setSelectedImage(null);
      if (fileInputRef.current) {
        fileInputRef.current.value = '';
      }
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const formatTimestamp = (timestamp) => {
    return new Date(timestamp).toLocaleTimeString([], { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  return (
    <div className="chat-interface">
      <div className="chat-header">
        <div className="chat-header-content">
          <div className="chat-header-text">
            <h2>Chat Assistant</h2>
            <p>Ask questions about your uploaded documents</p>
          </div>
          <button
            className="clear-chat-btn"
            onClick={clearChat}
            disabled={messages.length === 0 || isLoading}
            title={`Clear all chat history (${messages.length} messages)`}
          >
            <Trash2 size={18} />
            <span>Clear Chat</span>
            {messages.length > 0 && (
              <span className="message-count">({messages.length})</span>
            )}
          </button>
        </div>
      </div>

      <div className="chat-messages">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <h3>Welcome to your RAG Assistant!</h3>
            <p>Upload some documents and start asking questions about them.</p>
            <p>You can also upload images in your queries for multimodal assistance.</p>
          </div>
        ) : (
          messages.map((message, index) => (
            <div key={index} className={`message ${message.role}`}>
              <div className="message-content">
                {message.image && (
                  <div className="message-image">
                    <img 
                      src={message.image.dataUrl} 
                      alt={message.image.name}
                      style={{ maxWidth: '200px', maxHeight: '200px', borderRadius: '8px' }}
                    />
                    <p className="image-name">{message.image.name}</p>
                  </div>
                )}
                
                <div className="message-text">
                  {message.role === 'assistant' ? (
                    <ReactMarkdown>{message.content}</ReactMarkdown>
                  ) : (
                    <p>{message.content}</p>
                  )}
                </div>

                {message.sources && message.sources.length > 0 && (
                  <div className="message-sources">
                    <strong>Sources:</strong>
                    <ul>
                      {message.sources.map((source, idx) => (
                        <li key={idx}>{source}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
              
              <div className="message-timestamp">
                {formatTimestamp(message.timestamp)}
              </div>
            </div>
          ))
        )}
        
        {isLoading && (
          <div className="message assistant loading">
            <div className="message-content">
              <div className="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-container">
        {selectedImage && (
          <div className="selected-image-preview">
            <img 
              src={selectedImage.dataUrl} 
              alt={selectedImage.name}
              style={{ width: '60px', height: '60px', objectFit: 'cover', borderRadius: '4px' }}
            />
            <span className="image-name">{selectedImage.name}</span>
            <button 
              className="remove-image-btn"
              onClick={removeSelectedImage}
              title="Remove image"
            >
              <X size={16} />
            </button>
          </div>
        )}

        <div className="chat-input">
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleImageSelect}
            accept="image/*"
            style={{ display: 'none' }}
          />
          
          <button
            className="image-upload-btn"
            onClick={() => fileInputRef.current?.click()}
            title="Upload image"
            disabled={isLoading}
          >
            <Image size={20} />
          </button>

          <textarea
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask a question about your documents..."
            disabled={isLoading}
            rows={1}
            style={{ resize: 'none', overflow: 'hidden' }}
            onInput={(e) => {
              e.target.style.height = 'auto';
              e.target.style.height = Math.min(e.target.scrollHeight, 120) + 'px';
            }}
          />

          <button
            onClick={sendMessage}
            disabled={isLoading || (!inputMessage.trim() && !selectedImage)}
            className="send-btn"
            title="Send message"
          >
            <Send size={20} />
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;
