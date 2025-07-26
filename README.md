# KnowEdge Pro

## Project Overview

**KnowEdge Pro** is an AI-powered Knowledge Assistant built using a modern full-stack architecture. It implements Retrieval Augmented Generation (RAG) to provide intelligent question-answering capabilities over uploaded documents. The application consists of a **FastAPI backend** for document processing and AI services, and a **React frontend** for user interaction.

## Architecture

The project follows a **modular microservice architecture** with clear separation between frontend and backend services

- **Backend**: FastAPI-based Python application handling document processing, vector storage, and LLM integration
    
- **Frontend**: React-based single-page application providing user interface for document upload and chat functionality
    
- **Storage**: FAISS vector database for document embeddings and similarity search
    

## Quick Start Guide

## Prerequisites

- **Node.js** (version 14+ recommended)
    
- **Python** (version 3.7+ required)
    
- **npm** or **yarn** package manager

## Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/madhav2928/KnowEdge-Pro.git
cd KnowEdge-Pro
```

## 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

```bash
cp .env_template .env
# Edit .env file with your API keys and configuration
```


**Required Environment Variables**:

```text
##Use your own API keys, and embedding model of your choice, the model which I have given here can also be used, and for free API key you can create one from gemini AI studio


LLM_API_URL=https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=***********
LLM_API_METHOD=POST
LLM_API_KEY_HEADER=skip  


LLM_REQUEST_BODY_TEMPLATE='{"contents": [{"parts": [{"text": "{prompt}"}]}]}'
LLM_RESPONSE_JSON_PATH=candidates.0.content.parts.0.text

EMBEDDING_PROVIDER=huggingface
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

Start the FastAPI server:

```bash
# For development
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# For production
fastapi run main.py
```

The backend will be available at `http://127.0.0.1:8000`.

## 3. Frontend Setup

Open a new terminal and navigate to the frontend directory:

```bash
cd Frontend/knowedge-pro-frontend
```

Install Node.js dependencies:

```bash
npm install
```

Configure API base URL (optional):

```bash
# Create .env file in frontend directory
echo "REACT_APP_API_BASE=http://127.0.0.1:8000" > .env
```

Start the React development server:

```bash
npm start
```

The frontend will be available at `http://localhost:3000`.

## User Guide

## Getting Started

1. **Access the Application**: Open your web browser and navigate to `http://localhost:3000`
    
2. **Upload Documents**: Use the upload section to select and upload PDF documents for processing.
    
3. **Wait for Processing**: The system will process your document and create embeddings for search
    
4. **Start Chatting**: Use the chat interface to ask questions about your uploaded documents.

## Features

## Document Upload

- **Supported Formats**: PDF files
    
- **Processing**: Automatic text extraction and chunking
    
- **Storage**: Documents are converted to vector embeddings using sentence-transformers
    
- **Feedback**: Real-time status updates during upload and processing

## Chat Interface

- **Question Input**: Natural language queries about uploaded documents
    
- **AI Responses**: Contextual answers generated using RAG methodology
    
- **Markdown Support**: Rich text formatting in responses
    
- **Chat History**: Persistent conversation within the session

## Configuration

- **API Settings**: Configure LLM and embedding model parameters
    
- **Environment Variables**: Dynamic API base URL configuration based on deployment environment

## Best Practices

1. **Document Quality**: Upload clear, well-formatted PDF documents for best results
    
2. **Question Formulation**: Ask specific, contextual questions for more accurate responses
    
3. **File Size**: Keep PDF files under reasonable size limits for optimal processing speed
    
4. **Network**: Ensure stable internet connection for API calls

## Developer Documentation

## Project Structure

```text
KnowEdge-Pro/
├── Frontend/
│   └── knowedge-pro-frontend/
│       ├── public/
│       ├── src/
│       │   ├── components/
│       │   │   ├── UploadForm.jsx
│       │   │   ├── QueryForm.jsx
│       │   │   └── ConfigModal.jsx
│       │   ├── App.js
│       │   ├── config.js
│       │   └── index.js
│       ├── package.json
│       └── README.md
├── backend/
│   ├── embedding/
│   ├── llm/
│   ├── rag/
│   │   └── generator.py
│   ├── routes/
│   ├── utils/
│   ├── vectorstore/
│   ├── config.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env_template
└── .gitignore
```

## Backend Architecture

## Core Components

**1. FastAPI Application (`main.py`)**

- Main application entry point
    
- CORS middleware configuration
    
- Router integration
    
- Debug endpoints for development

**2. RAG System (`rag/generator.py`)**

- Document retrieval using FAISS vector search
    
- Context preparation for LLM
    
- Answer generation pipeline

**3. Vector Storage (`vectorstore/`)**

- FAISS-based similarity search
    
- Document embedding storage
    
- Retrieval functionality

**4. LLM Integration (`llm/`)**

- Configurable LLM providers
    
- Request/response handling
    
- Error management

**5. Routes (`routes/`)**

- `/upload/`: Document upload and processing
    
- `/query`: Question answering endpoint
    
- `/byok`: Configuration management

## API Endpoints

**Upload Endpoint**

```text
POST /upload/
Content-Type: multipart/form-data
Body: file (PDF)
Response: {"chunks_stored": number}
```

**Query Endpoint**

```text
POST /query
Content-Type: application/x-www-form-urlencoded
Body: query=your_question
Response: {"answer": "AI response"}
```

**Debug Endpoint**

```text
GET /debug/chunks
Response: {"chunks": [{"id": int, "text": string, "embedding": array}]}
```

## Frontend Architecture

## Component Structure

**1. App Component (`App.js`)**

- Main application layout
    
- State management for configuration modal
    
- Component orchestration

**2. UploadForm Component (`UploadForm.jsx`)**

- File selection and upload functionality
    
- Progress tracking and status updates
    
- Integration with backend upload API

**3. QueryForm Component (`QueryForm.jsx`)**

- Chat interface implementation
    
- Message state management
    
- Markdown rendering for responses

**4. ConfigModal Component**

- API configuration interface
    
- Environment-specific settings
    

## State Management

The application uses React's built-in state management with `useState` hooks for:

- File upload status
    
- Chat conversation history
    
- Configuration modal visibility
    
- API response handling

## Contributing

## Development Setup

1. Fork the repository
    
2. Create a feature branch
    
3. Follow coding standards and add tests
    
4. Submit a pull request with detailed description

## Code Style

- **Python**: Follow PEP 8 standards with black formatting
    
- **JavaScript**: Follow Airbnb style guide with ESLint
    
- **Documentation**: Use clear, concise comments and docstrings
