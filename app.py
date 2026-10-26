
import streamlit as st

from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate


st.set_page_config(page_title="YouTube RAG Chatbot", page_icon="🤖")

st.title("🤖 YouTube RAG Chatbot")
st.write("Ask questions about the YouTube video!")

Video_id = "d4yCWBGFCEs"

@st.cache_resource
def create_retriever(video_id):

    yt_api = YouTubeTranscriptApi()

    transcripts = yt_api.fetch(
        video_id,
        languages=["en", "hi"]
    )

    # Convert transcript snippets into plain text
    transcript_text = " ".join(
        snippet.text for snippet in transcripts
    )

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80
    )

    chunks = splitter.split_text(transcript_text)

    # Create embeddings
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    # Create FAISS vector database
    vector_store = FAISS.from_texts(
        chunks,
        embeddings
    )

    # Create retriever
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 2}
    )

    return retriever


# 3. Create prompt template
prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Answer the question using ONLY the context below.
If the context is insufficient, say:
"I don't know based on this video transcript."

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)


# 4. Load chat model
@st.cache_resource
def load_llm():
    return ChatOllama(
        model="llama3.2",
        temperature=0.2
    )


# 5. User input
question = st.chat_input("Type your question here...")


# 6. Process question
if question:

    with st.spinner("Searching video transcript..."):

        try:
            retriever = create_retriever(Video_id)

            # Retrieve relevant documents
            context_docs = retriever.invoke(question)

            # Combine document text
            contexts = " ".join(
                doc.page_content for doc in context_docs
            )

            # Format the prompt
            final_prompt = prompt.invoke({
                "context": contexts,
                "question": question
            })

            # Generate answer
            llm = load_llm()
            answer = llm.invoke(final_prompt)

            # Display only answer text
            st.subheader("Answer")
            st.write(answer.content)

            # Optional: display retrieved context
            with st.expander("View retrieved context"):
                st.write(contexts)

        except Exception as e:
            st.error(
                f"Error: {type(e).__name__}: {e}"
            )
