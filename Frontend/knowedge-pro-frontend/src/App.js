import React, { useState } from 'react';
import UploadForm from './components/UploadForm';
import QueryForm from './components/QueryForm';
import ConfigModal from './components/ConfigModal';
import './App.css'; // 👈 Import CSS

function App() {
  const [showConfig, setShowConfig] = useState(false);
  return (
    <div className="app">
      <div className="app-container">
        <div className="header-bar">
          <h1>KnowEdge Pro</h1>
          <span className="subtitle">AI Knowledge Assistant</span>
          <button className="config-btn" onClick={() => setShowConfig(true)} title="Settings">
            ⚙️
          </button>
        </div>
        <ConfigModal show={showConfig} onClose={() => setShowConfig(false)} />
        <hr />
        <UploadForm />
        <hr />
        <QueryForm />
      </div>
    </div>
  );
}

export default App;
