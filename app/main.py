import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

# Load FAISS vector store
@st.cache_resource
def load_vectorstore():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local("embeddings/iam_faiss_index", embedding, allow_dangerous_deserialization=True)

vectorstore = load_vectorstore()

# Load the text generation model
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

qa_model = load_model()

# App UI
st.title("🔐 IAM Log Q&A Bot")
st.markdown("Ask questions about IAM access logs using GenAI.")

user_input = st.text_input("❓ Ask your question:")

if user_input:
    # Retrieve context
    docs = vectorstore.similarity_search(user_input, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    # Generate answer
    prompt = f"Context: {context}\n\nQuestion: {user_input}\n\nAnswer:"
    result = qa_model(prompt, max_length=100)[0]['generated_text']

    # Show result
    st.markdown("### 📚 Retrieved Context")
    st.code(context)

    st.markdown("### 💬 Generated Answer")
    st.success(result)
