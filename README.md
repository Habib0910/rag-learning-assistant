# RAG Learning Assistant

A Retrieval-Augmented Generation (RAG) learning assistant that helps users find where specific topics are taught in a web development video course.

The project processes Hindi educational videos, converts speech to text using OpenAI Whisper, creates semantic embeddings, retrieves the most relevant video sections using cosine similarity, and uses Llama 3.2 to generate an answer with relevant video timestamps.

## Features

- Hindi speech-to-text and translation using OpenAI Whisper
- Video transcript segmentation into timestamped chunks
- Semantic embeddings using Ollama
- Similarity search using cosine similarity
- Retrieval of the most relevant video sections
- Llama 3.2 for generating natural-language responses
- Provides relevant video numbers and timestamps for learning

## Project Pipeline

```text
Hindi Course Videos
        ↓
   Audio Extraction
        ↓
   OpenAI Whisper
        ↓
 Timestamped Text Chunks
        ↓
   Semantic Embeddings
        ↓
 Cosine Similarity Search
        ↓
 Top Relevant Chunks
        ↓
     Llama 3.2
        ↓
 Learning Assistant Response
```

## Technologies Used

- Python
- OpenAI Whisper
- Ollama
- Llama 3.2
- Nomic Embed Text
- NumPy
- Pandas
- Scikit-learn
- Joblib
- Requests
- FFmpeg

## How It Works

1. Course videos are converted into audio files.
2. Whisper processes the Hindi audio and translates it into English text.
3. The transcript is divided into timestamped chunks.
4. Each chunk is converted into a numerical embedding.
5. When a user asks a question, the question is also converted into an embedding.
6. Cosine similarity is used to find the most relevant video chunks.
7. The top matching chunks are provided to Llama 3.2.
8. The model generates a response indicating which video and timestamp contain the relevant information.

## Example

A user can ask:

> Where are HTML input tags taught in the course?

The system retrieves the most relevant video sections and provides the video number and timestamp where the topic is discussed.

## Project Structure

```text
rag-learning-assistant/
│
├── abc.py
├── createchunks.py
├── proces_incoming.py
├── read_chunks.py
├── read_chunkstryy.py
├── speech_to_text.py
├── .gitignore
└── README.md
```

## Local Requirements

This project requires:

- Python 3
- FFmpeg
- Ollama
- Llama 3.2
- Nomic Embed Text

The large video, audio, Whisper model, generated embeddings, and course transcript data are intentionally excluded from the repository.

## Future Improvements

- Build a user-friendly web interface
- Improve retrieval accuracy
- Add conversation memory
- Support more courses and languages
- Add automated evaluation of retrieved answers