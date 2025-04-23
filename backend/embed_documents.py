from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# Load and split documents
loader = TextLoader("data/iam_policy_sample.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
docs = splitter.split_documents(documents)

# Use Hugging Face embeddings
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embedding_model)

# Save vectorstore
vectorstore.save_local("embeddings/iam_faiss_index")

print("✅ Embeddings created and FAISS index saved.")
