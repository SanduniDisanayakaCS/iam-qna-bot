# 💬 IAM Log Q&A Bot (LangChain + Hugging Face + Streamlit)

[![Streamlit App](https://img.shields.io/badge/🚀_Live_App-Click_to_View-green?logo=streamlit)](https://iam-qna-bot-version2.streamlit.app)

An AI-powered chatbot that answers natural language questions about IAM access logs. Built using **LangChain**, **Hugging Face Transformers**, **FAISS**, and deployed with **Streamlit Cloud**.

---

## 🧠 What It Does

- 🔍 Retrieves relevant log lines using vector similarity (FAISS)
- 🤖 Answers in natural language using `flan-t5-base`
- 🧾 Supports IAM access logs (CloudTrail style)
- 🌍 Fully deployable — no OpenAI key required

---

## 🛠 Tech Stack

| Component           | Tech                          |
|---------------------|-------------------------------|
| Embeddings          | `all-MiniLM-L6-v2` via Hugging Face  
| Vector DB           | FAISS (in-memory, local)  
| Generation Model    | `google/flan-t5-base` (Hugging Face)  
| Framework           | LangChain + Transformers  
| Frontend            | Streamlit  
| Hosting             | Streamlit Cloud  

---

## 📂 Folder Structure

iam-qna-bot/ ├── app/ # Streamlit frontend │ └── main.py ├── backend/ # Embedding + Retrieval logic │ ├── embed_documents.py │ └── retrieve_context.py ├── data/ # Sample IAM logs │ └── iam_policy_sample.txt ├── embeddings/ # FAISS vector DB │ └── iam_faiss_index/ ├── requirements.txt └── README.md


---

## 🧪 Example Q&A

**Q:** Who failed while deleting a bucket?  
**📚 Retrieved Context:**
[ERROR] 2024-12-01T12:50:00Z - User: eve - Action: DeleteBucket - Status: Unauthorized


**💬 Generated Answer:**
eve


---


---

## 🚀 Run Locally

```bash
git clone https://github.com/SanduniDisanayakaCS/iam-qna-bot.git
cd iam-qna-bot
python -m venv .venv
.venv\Scripts\activate    # (use `source .venv/bin/activate` on Mac/Linux)
pip install -r requirements.txt

streamlit run app/main.py

---

## 👩‍💻 Author

**Sanduni Disanayaka**  
📧 [sandunidisanayaka96@gmail.com](mailto:sandunidisanayaka96@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/sanduni-disanayaka-3073b1240/)  
💻 [GitHub](https://github.com/SanduniDisanayakaCS)

---

## 🔗 Project Links

🧠 [Source Code (GitHub)](https://github.com/SanduniDisanayakaCS/iam-qna-bot)  
🚀 [Live App (Streamlit)](https://iam-qna-bot-version2.streamlit.app)



