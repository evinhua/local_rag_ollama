import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, File, Trash2, CheckCircle, XCircle } from 'lucide-react';
import './DocumentUpload.css';

const DocumentUpload = ({ documents, onDocumentUploaded, onClearDocuments }) => {
  const [uploading, setUploading] = useState(false);
  const [uploadStatus, setUploadStatus] = useState(null);

  const onDrop = async (acceptedFiles) => {
    const file = acceptedFiles[0];
    if (!file) return;

    setUploading(true);
    setUploadStatus(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/upload', {
        method: 'POST',
        body: formData,
      });

      const result = await response.json();
      
      if (response.ok) {
        setUploadStatus({
          type: 'success',
          message: `Successfully uploaded ${result.filename} (${result.chunks_created} chunks created)`
        });
        onDocumentUploaded(result);
      } else {
        setUploadStatus({
          type: 'error',
          message: result.detail || 'Upload failed'
        });
      }
    } catch (error) {
      setUploadStatus({
        type: 'error',
        message: `Upload failed: ${error.message}`
      });
    } finally {
      setUploading(false);
    }
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
      'application/vnd.openxmlformats-officedocument.presentationml.presentation': ['.pptx']
    },
    multiple: false,
    disabled: uploading
  });

  const getFileIcon = (fileType) => {
    switch (fileType) {
      case 'pdf':
        return '📄';
      case 'docx':
        return '📝';
      case 'pptx':
        return '📊';
      default:
        return '📄';
    }
  };

  return (
    <div className="document-upload">
      <h2>Documents</h2>
      
      {/* Upload Area */}
      <div
        {...getRootProps()}
        className={`upload-area ${isDragActive ? 'drag-active' : ''} ${uploading ? 'uploading' : ''}`}
      >
        <input {...getInputProps()} />
        <Upload size={32} />
        {uploading ? (
          <p>Uploading...</p>
        ) : isDragActive ? (
          <p>Drop the file here...</p>
        ) : (
          <div>
            <p>Drag & drop a document here</p>
            <p className="upload-hint">or click to select</p>
            <p className="supported-formats">Supports: PDF, DOCX, PPTX</p>
          </div>
        )}
      </div>

      {/* Upload Status */}
      {uploadStatus && (
        <div className={`upload-status ${uploadStatus.type}`}>
          {uploadStatus.type === 'success' ? (
            <CheckCircle size={16} />
          ) : (
            <XCircle size={16} />
          )}
          <span>{uploadStatus.message}</span>
        </div>
      )}

      {/* Document List */}
      <div className="document-list">
        <div className="document-list-header">
          <h3>Uploaded Documents ({documents.length})</h3>
          {documents.length > 0 && (
            <button 
              className="clear-button"
              onClick={onClearDocuments}
              title="Clear all documents"
            >
              <Trash2 size={16} />
            </button>
          )}
        </div>

        {documents.length === 0 ? (
          <p className="no-documents">No documents uploaded yet</p>
        ) : (
          <div className="documents">
            {documents.map((doc) => (
              <div key={doc.document_id} className="document-item">
                <div className="document-icon">
                  {getFileIcon(doc.file_type)}
                </div>
                <div className="document-info">
                  <div className="document-name" title={doc.filename}>
                    {doc.filename}
                  </div>
                  <div className="document-meta">
                    {doc.file_type.toUpperCase()} • {doc.chunks} chunks
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default DocumentUpload;
