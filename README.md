# YouTube RAG Chatbot 🎥🤖

A Generative AI-powered chatbot that answers questions about YouTube videos using their transcripts. Built with Python, Streamlit, LangChain, Ollama, and FAISS, this project uses Retrieval-Augmented Generation (RAG) to retrieve relevant transcript sections and generate contextual answers.

## 🚀 Features

- **YouTube Transcript Extraction:** Fetches available video transcripts.
- **Text Chunking:** Splits transcripts into smaller, overlapping chunks.
- **Text Embeddings:** Uses Ollama's `nomic-embed-text` model to convert text into embeddings.
- **Vector Database:** Stores embeddings and retrieves relevant content using FAISS.
- **AI-Powered Answers:** Uses the `llama3.2` model through Ollama to answer questions.
- **Interactive UI:** Provides a simple Streamlit chat interface.
- **Context-Based Responses:** Instructs the model to answer using retrieved transcript context.
- **Error Handling:** Displays helpful messages when transcript fetching or model execution fails.

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Ollama
- Llama 3.2
- Nomic Embed Text
- FAISS
- YouTube Transcript API

## 📁 Project Structure

```text
YouTube-RAG-Chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YouTube-RAG-Chatbot
```


### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

Add these packages to `requirements.txt`:

```text
streamlit
youtube-transcript-api
langchain-core
langchain-community
langchain-text-splitters
langchain-ollama
faiss-cpu
```

Install them:

```bash
pip install -r requirements.txt
```

### 4. Install Ollama models

Install Ollama from https://ollama.com/ and run:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

For a potentially faster response, you can try the smaller model:

```bash
ollama pull llama3.2:1b
```

If you use this smaller model, update the model name in your Python code accordingly.

### 5. Run the application

```bash
streamlit run app.py
```


## 💬 How to Use

1. Start the Streamlit application.
2. Ensure Ollama is running and the required models are installed.
3. The app fetches the transcript for the configured YouTube video.
4. Enter a question about the video's content.
5. The retriever finds relevant transcript chunks.
6. The language model generates an answer based on the retrieved context.

## ⚡ Performance Improvements

- Cache the FAISS retriever using `st.cache_resource`.
- Reuse the loaded Ollama model.
- Retrieve only the most relevant chunks, such as `k=2`.
- Limit the generated answer length with `num_predict`.
- Use streaming to display answers as they are generated.
- Avoid fetching and embedding the same transcript for every question.

### Ollama model not found

Pull the model used in your code:

```bash
ollama pull llama3.2
```

### FAISS or LangChain module not found

Install the dependencies again:

```bash
pip install -r requirements.txt
```

### No transcript available

Some videos do not have accessible captions in the requested language. Use another video or provide a transcript text file.

## 🔮 Future Improvements

- Allow users to paste any supported YouTube URL.
- Add transcript upload support for `.txt` and `.vtt` files.
- Add chat history and conversation memory.
- Display source transcript chunks alongside answers.
- Support multiple videos in one knowledge base.
- Improve retrieval using reranking and hybrid search.
- Add a transcript summarization feature.
- Improve the interface with a sidebar, video metadata, and response-time metrics.

## 🎯 Project Objective

The objective of this project is to demonstrate how Retrieval-Augmented Generation can connect a language model to external textual information, enabling users to ask natural-language questions about video content.

## 📜 License

This project is intended for educational and personal learning purposes. Add a suitable open-source license if you intend to distribute the code publicly.
