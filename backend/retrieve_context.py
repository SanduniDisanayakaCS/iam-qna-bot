from transformers import pipeline
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI  # Optional if you plan to generate answers
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def retrieve_answer(question: str):
    # Load FAISS vectorstore inside the function
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local("embeddings/iam_faiss_index", embedding_model, allow_dangerous_deserialization=True)

    # Perform similarity search
    docs = vectorstore.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    print("\n📚 Retrieved Context:")
    print(context)

    print("\n❓ User Question:")
    print(question)

    return context


# For manual test
if __name__ == "__main__":
    q = input("Ask a question about the IAM logs: ")
    context = retrieve_answer(q)

    from transformers import pipeline

    # Load the model for generating answers
    qa_model = pipeline("text2text-generation", model="google/flan-t5-base")

    # Build the prompt
    prompt = f"Context: {context}\n\nQuestion: {q}\n\nAnswer:"

    # Generate the answer
    result = qa_model(prompt, max_length=100)[0]['generated_text']

    print("\n💬 Generated Answer:")
    print(result)



