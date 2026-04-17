🚀 AI Meeting Intelligence System

An end-to-end AI-powered web application that records meeting audio, transcribes it using speech recognition, and enables intelligent querying over the meeting using Retrieval-Augmented Generation (RAG).

🧠 Features
🎙️ Real-time Audio Recording (Web App)
Capture meeting audio directly from the browser using MediaRecorder API
📝 Speech-to-Text Transcription
Converts audio into text using OpenAI Whisper
🧩 Semantic Search with FAISS
Splits transcripts into chunks and retrieves relevant context using vector similarity search
🤖 Local LLM Integration
Uses Ollama (LLaMA 3) for:
Meeting summaries
Context-aware question answering
🔍 RAG-based Chatbot
Ask questions about the meeting and get precise answers based on actual discussion
⚙️ Tech Stack
Frontend: HTML, JavaScript (MediaRecorder API)
Backend: Python, Flask
AI Models:
OpenAI Whisper (Transcription)
sentence-transformers (Embeddings)
FAISS (Vector Search)
Ollama (LLM Inference)
🧠 How It Works
Browser Mic → Audio Recording → Flask Backend
        ↓
Whisper → Transcript
        ↓
Chunking → Embeddings → FAISS Index
        ↓
User Query → Relevant Chunk Retrieval
        ↓
Ollama → Final Answer
🎯 Use Cases
Meeting summarization
Extracting key insights and decisions
Searching past discussions
AI-powered meeting assistant
🚀 Future Improvements
Speaker diarization (who said what)
Multi-meeting memory
Real-time transcription
Streamlit / React UI upgrade
📌 Key Learning Outcomes
Built an end-to-end RAG pipeline
Implemented semantic search using FAISS
Integrated local LLMs for inference
Designed a full-stack AI-powered web application
