# AI Video Assistant

AI Video Assistant is a Python-based meeting intelligence app that ingests a YouTube video or local audio/video file, transcribes it, extracts actionable summaries, and lets you ask questions about the conversation using a lightweight RAG pipeline.

It is designed to help users turn long recordings into structured insights like meeting summaries, decisions, action items, and follow-up questions.

## Features

- YouTube URL or local file ingestion
- Audio download and conversion to WAV
- Audio chunking for large recordings
- Transcription with Whisper for English and Sarvam for Hinglish/translated workflows
- AI-generated meeting title
- Meeting summary generation
- Extraction of:
  - action items
  - key decisions
  - open questions
- Retrieval-augmented chat over the transcript
- Streamlit web UI and simple CLI support

## Tech Stack

- Python 3.10+
- Streamlit
- Whisper
- PyDub, yt-dlp, ffmpeg
- LangChain + Mistral AI
- ChromaDB + Hugging Face embeddings
- Deep-translator, requests, numpy

## Repository Structure

```text
AI-Video-Assistant-/
├── app.py                  # Streamlit web application
├── main.py                 # CLI pipeline runner
├── Requirements.txt        # Python dependencies
├── .gitignore
├── core/
│   ├── extractor.py       # Action items / decisions / questions extraction
│   ├── rag_engine.py       # RAG pipeline using LangChain + Chroma
│   ├── summarizer.py       # Meeting summaries and title generation
│   ├── transcriber.py      # Whisper / Sarvam transcription orchestration
│   └── vector_store.py     # Chroma vector store setup and retrieval
├── utils/
│   └── audio_processor.py  # Download, convert, and chunk audio
├── downloades/            # Generated audio output directory
├── vector_db/             # Chroma persistence directory
├── README.md              # Project documentation
└── test.py                # Test or example script
