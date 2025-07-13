import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import './QueryForm.css';

const QueryForm = () => {
  const [query, setQuery] = useState('');
  const [chat, setChat] = useState([]);

  const handleAsk = async () => {
    if (!query.trim()) return;

    const updatedChat = [...chat, { role: 'user', text: query }];
    setChat(updatedChat);
    setQuery('');

    const response = await fetch('http://127.0.0.1:8000/query', {
      method: 'POST',
      body: new URLSearchParams({ query }),
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });

    const data = await response.json();
    setChat([...updatedChat, { role: 'bot', text: data.answer }]);
  };

  const clearChat = () => {
    setChat([]);
  };

  
  return (
    <div className="chat-container">
      <h2>Chat with KnowEdge Pro</h2>

    <div className="chat-controls">
        <button className="refresh-button" onClick={clearChat} title="Refresh Chat">
        ⟳
        </button>
    </div>
        {chat.length > 0 && (
            <div className="chat-window">
                {chat.map((msg, i) => (
                <div
                    key={i}
                    className={`chat-bubble ${msg.role === 'user' ? 'user' : 'bot'}`}
                >
                    {msg.role === 'bot' ? (
                    <ReactMarkdown>{msg.text}</ReactMarkdown>
                    ) : (
                    <>
                        <strong>You:</strong> {msg.text}
                    </>
                    )}
                </div>
                ))}
            </div>
            )}
      <div className="chat-input">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask your question..."
        />
        <button onClick={handleAsk}>Send</button>
      </div>
    </div>
  );
};

export default QueryForm;
