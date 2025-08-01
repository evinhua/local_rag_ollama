import React, { useState, useEffect } from 'react';
import DocumentUpload from './components/DocumentUpload';
import ChatInterface from './components/ChatInterface';
import StatusBar from './components/StatusBar';
import './App.css';

function App() {
  const [documents, setDocuments] = useState([]);
  const [systemStatus, setSystemStatus] = useState({
    status: 'unknown',
    ollama_status: 'unknown',
    chroma_status: 'unknown'
  });

  // Check system health on startup
  useEffect(() => {
    checkSystemHealth();
    loadDocuments();
  }, []);

  const checkSystemHealth = async () => {
    try {
      const response = await fetch('/health');
      const data = await response.json();
      setSystemStatus(data);
    } catch (error) {
      console.error('Health check failed:', error);
      setSystemStatus({
        status: 'error',
        ollama_status: 'error',
        chroma_status: 'error'
      });
    }
  };

  const loadDocuments = async () => {
    try {
      const response = await fetch('/documents');
      const data = await response.json();
      setDocuments(data.documents || []);
    } catch (error) {
      console.error('Failed to load documents:', error);
    }
  };

  const handleDocumentUploaded = (newDocument) => {
    if (newDocument.success) {
      loadDocuments(); // Refresh document list
    }
  };

  const handleClearDocuments = async () => {
    if (window.confirm('Are you sure you want to clear all documents?')) {
      try {
        await fetch('/documents', { method: 'DELETE' });
        setDocuments([]);
      } catch (error) {
        console.error('Failed to clear documents:', error);
      }
    }
  };

  return (
    <div className="App">
      <header className="app-header">
        <h1>Local RAG Assistant</h1>
        <StatusBar status={systemStatus} onRefresh={checkSystemHealth} />
      </header>
      
      <div className="app-content">
        <div className="left-panel">
          <DocumentUpload 
            documents={documents}
            onDocumentUploaded={handleDocumentUploaded}
            onClearDocuments={handleClearDocuments}
          />
        </div>
        
        <div className="right-panel">
          <ChatInterface />
        </div>
      </div>
    </div>
  );
}

export default App;
