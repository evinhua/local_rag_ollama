import React from 'react';
import { RefreshCw, CheckCircle, XCircle, AlertCircle } from 'lucide-react';
import './StatusBar.css';

const StatusBar = ({ status, onRefresh }) => {
  const getStatusIcon = (statusValue) => {
    switch (statusValue) {
      case 'healthy':
        return <CheckCircle size={16} className="status-icon healthy" />;
      case 'unhealthy':
      case 'error':
        return <XCircle size={16} className="status-icon unhealthy" />;
      case 'degraded':
        return <AlertCircle size={16} className="status-icon degraded" />;
      default:
        return <AlertCircle size={16} className="status-icon unknown" />;
    }
  };

  const getStatusText = (statusValue) => {
    switch (statusValue) {
      case 'healthy':
        return 'Healthy';
      case 'unhealthy':
      case 'error':
        return 'Error';
      case 'degraded':
        return 'Degraded';
      default:
        return 'Unknown';
    }
  };

  return (
    <div className="status-bar">
      <div className="status-items">
        <div className="status-item">
          <span className="status-label">System:</span>
          {getStatusIcon(status.status)}
          <span className="status-text">{getStatusText(status.status)}</span>
        </div>

        <div className="status-item">
          <span className="status-label">Ollama:</span>
          {getStatusIcon(status.ollama_status)}
          <span className="status-text">{getStatusText(status.ollama_status)}</span>
        </div>

        <div className="status-item">
          <span className="status-label">Chroma:</span>
          {getStatusIcon(status.chroma_status)}
          <span className="status-text">{getStatusText(status.chroma_status)}</span>
        </div>
      </div>

      <button 
        className="refresh-btn"
        onClick={onRefresh}
        title="Refresh status"
      >
        <RefreshCw size={16} />
      </button>
    </div>
  );
};

export default StatusBar;
