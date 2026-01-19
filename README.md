# 🧠 Customer Response Agent (Agentic AI with Langchain)

An **agentic AI system** that automatically processes customer emails related to orders, fetches order details using tools, drafts a **customer-addressed response**, and sends it for **human review** — all exposed via a **FastAPI backend**.

This project demonstrates **production-grade Agentic AI** using **LangChain**, tool calling, structured prompting, and backend integration.

---

## ✨ Key Features

* 🤖 **LLM-powered customer support agent**
* 🧩 **Agentic workflow** (reason → act → respond)
* 🛠️ **Tool calling** (order lookup, human review request)
* 🚀 **FastAPI API** for real-world usage
* 🔐 Clean architecture (no hardcoded secrets)

---

## 🧱 Architecture Overview

```
Customer Email
     ↓
FastAPI Endpoint
     ↓
Langchain Agent
 ├─ Extract Order ID & Issue
 ├─ Call Order DB Tool
 ├─ Draft Polite Response (User-addressed)
 └─ Call Human Review Tool
     ↓
Final Draft Response
```

---

## 📁 Project Structure

```
customer-response-agent/
│── main.py              # FastAPI app
│── agent.py             # Langchain agent logic
│── tools.py             # Tool definitions (DB, review)
│── requirements.txt     # Dependencies
│── .gitignore
│── README.md
```

---

## ⚙️ Tech Stack

* **Python 3.10+**
* **FastAPI** – API layer
* **LangChain** – agent + tool abstractions
* **Google Gemini 2.5 Flash** – LLM
* **Uvicorn** – ASGI server

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/customer-response-agent.git
cd customer-response-agent
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set environment variables

Create a `.env` file (recommended):

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

❗ Never hardcode API keys in source files.

---

## 🚀 Running the Application

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📩 API Usage Example

### Endpoint

```
POST /process-email
```

### Request Body

```json
{
  "email": "I ordered a blue KitchenPro blender (Order #8847) but received a red toaster instead."
}
```

---

### Sample Response

```json
{
  "response": "Dear Susan,\n\nThank you for contacting us regarding your recent order (#8847). I’m very sorry to hear that you received a red toaster instead of the blue KitchenPro blender you ordered..."
}
```

✔️ Response is **directly addressed to the customer**
✔️ Polite, professional tone
✔️ Escalated for human review

---

## 🧠 Agent Behavior (Important)

The agent follows **strict steps**:

1. Extract order ID and issue from email
2. Fetch order details via tool
3. Draft a **customer-facing email** (not an internal summary)
4. Send draft for human review

This avoids:

* ❌ Meta explanations
* ❌ Internal summaries
* ❌ Agent self-commentary

---

## 🛠️ Tools Used

### 🔍 orders_database_query

* Simulates fetching order details
* Accepts `order_id`
* Returns order metadata

### 🧑‍💼 request_review

* Flags response for human approval
* Used as final step in agent flow

---

## 🧪 Common Errors & Fixes

### ❌ `InvalidUpdateError: Expected dict`

**Cause:** Agent node returning a string instead of dict

**Fix:**
Ensure agent returns:

```python
{"response": result}
```

---

### ❌ `ValueError: contents are required`

**Cause:** LLM invoked with empty or malformed messages

**Fix:**
Use structured input:

```python
agent.invoke({"input": prompt})
```

---

## 🔐 Security Notes

* API keys via environment variables only
* `.gitignore` includes:

  * `venv/`
  * `.env`
  * `__pycache__/`

---

## 🌱 Future Improvements

* ✅ Database integration (PostgreSQL)
* ✅ Email sending (SMTP / SendGrid)
* ✅ Authenticated admin dashboard
* ✅ Memory per customer
* ✅ SLA-based routing

---


## 👤 Author

**Dipta Chatterjee**
AI / Data Scientist

---

⭐ If you found this useful, consider starring the repo.
