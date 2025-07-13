import React, { useState } from 'react';
import axios from 'axios';
import './UploadForm.css';
function UploadForm({ onUploadComplete }) {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setUploadStatus('');
  };

  const handleClearFile = () => {
    setFile(null);
    setUploadStatus('');
    document.getElementById('fileInput').value = ''; // reset native input
  };

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await axios.post('http://127.0.0.1:8000/upload/', formData);
      setUploadStatus(`✅ Uploaded: ${res.data.chunks_stored} chunks stored.`);
      onUploadComplete && onUploadComplete();
    } catch (error) {
      setUploadStatus('❌ Upload failed');
      console.error(error);
    }
  };

  return (
    <div className='chat-container'>
        <h2>Upload documents necessary for research</h2>
    <hr />
    <div className="upload-form-wrapper">
      <input
        id="fileInput"
        type="file"
        onChange={handleFileChange}
        style={{ display: 'none' }}
      />
      {!file ? (
        <label htmlFor="fileInput" className="file-picker">
          📘 Choose a PDF to Upload
        </label>
      ) : (
        <div className="file-display">
          <span className="file-name">📘 {file.name}</span>
          <button className="remove-btn" onClick={handleClearFile} title="Remove file">
            ✖
            </button>
        </div>
      )}

      <button onClick={handleUpload} className="upload-button">
        Upload
      </button>

      {uploadStatus && <p className="upload-status">{uploadStatus}</p>}
    </div>
    </div>
  );
}

export default UploadForm;
