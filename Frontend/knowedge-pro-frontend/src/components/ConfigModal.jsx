import React, { useState } from 'react';
import './ConfigModal.css';
import API_BASE from '../config';

const ConfigModal = ({ show, onClose }) => {
  const [formData, setFormData] = useState({
    LLM_API_URL: '',
    LLM_API_METHOD: '',
    LLM_API_KEY_HEADER: '',
    LLM_REQUEST_BODY_TEMPLATE: '',
    LLM_RESPONSE_JSON_PATH: '',
    EMBEDDING_PROVIDER: '',
    EMBEDDING_MODEL: ''
  });

  const [responseMessage, setResponseMessage] = useState('');
  const [showToast, setShowToast] = useState(false);
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleUpdate = async () => {
    const updates = {};
    for (const key in formData) {
      if (formData[key]) updates[key] = formData[key];
    }
  
    try {
      const res = await fetch(`${API_BASE}/byok/config/bulk-update`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ updates }),
      });
  
      const resultText = await res.text(); // or `await res.json()` if JSON
  
      setResponseMessage(resultText);
      setShowToast(true);
  
      // Auto-hide after 3 seconds
      setTimeout(() => {
        setShowToast(false);
        setResponseMessage('');
        onClose(); // Close modal only after showing message
      }, 3000);
    } catch (err) {
      setResponseMessage('Error updating config.');
      setShowToast(true);
      setTimeout(() => {
        setShowToast(false);
        setResponseMessage('');
      }, 3000);
    }
  };

  if (!show) return null;

  return (
    <div className="config-modal-overlay">
      <div className="config-modal">
        <div className="config-modal-header">
          <h2>Update Config (For now it runs on default values)</h2>
          <button className="close-btn" onClick={onClose}>✖</button>
        </div>
        <div className="config-modal-body">
          {Object.keys(formData).map((key) => (
            <div key={key} className="form-group">
              <label>{key}</label>
              <input
                type="text"
                name={key}
                placeholder={`Enter ${key}`}
                value={formData[key]}
                onChange={handleChange}
              />
            </div>
          ))}
        </div>
        <div className="config-modal-footer">
          <button className="update-btn" onClick={handleUpdate}>Update</button>
        </div>
      </div>
      {showToast && (
        <div className="toast-message">
            {responseMessage}
        </div>
    )}
    </div>
  );
};

export default ConfigModal;
