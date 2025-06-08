# 🧠 AI Research Assistant System

This is a full-stack AI system designed to act as an intelligent research assistant using:
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Multi-Agent AI Architecture
- ✅ LLMOps concepts
- ✅ Fine-Tuning (LoRA)
- ✅ LangChain and OpenAI API integrations
- ✅ Modern frontend (React + Tailwind) and backend (FastAPI + FAISS)

---

## 🚀 Project Features

| Feature                      | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| **Document Upload**         | Users can upload PDFs which are parsed, chunked, and embedded               |
| **RAG**                     | Semantic search using vector embeddings + context-based generation         |
| **Multi-Agent System**      | Dedicated agents (e.g., summarizer, evaluator) triggered based on input    |
| **Fine-Tuning**             | LoRA-based fine-tuning pipelines via notebooks                             |
| **LangChain Integration**   | Modular chains for parsing, QA, summarizing                                |
| **LLMOps Tools**            | Includes tracking (monitor.py), logs, model registry (model_tracker.py)   |

---

## 🗂️ Folder Structure & File Explanations

### 📦 `backend/`

#### 📁 `api/`
- `main.py` – Starts FastAPI app, mounts routers.
- `routes/query.py` – Endpoint for answering user questions.
- `routes/upload.py` – Endpoint for uploading and processing files.
- `dependencies.py` – Common DI setups (embedding models, FAISS, etc).

#### 📁 `agents/`
- `base_agent.py` – Blueprint for all agents (summarizer, fine-tuner).
- `multi_agent_executor.py` – Agent dispatcher logic.
- `tools.py` – Shared tools/helpers used across agents.

#### 📁 `rag/` (Retrieval-Augmented Generation)
- `embedder.py` – SentenceTransformer wrapper.
- `vector_store.py` – FAISS index load/save/search logic.
- `document_loader.py` – Extracts and chunks text from uploaded files.
- `retriever.py` – Uses query to retrieve top-k similar chunks.

#### 📁 `llm/`
- `openai_client.py` – Communicates with OpenAI API.
- `fine_tuned_model.py` – Logic for fine-tuned model inference (LoRA).
- `response_generator.py` – Unified logic that combines RAG + LLM.

#### 📁 `ops/` (LLMOps)
- `logger.py` – Custom logging.
- `monitor.py` – Tracks ongoing queries and agents.
- `model_tracker.py` – Keeps track of fine-tuned models, versions, tags.

#### 📁 `config/`
- `settings.py` – Loads `.env` file values, configs.
- `constants.py` – Static values used throughout the system.

#### 📁 `utils/`
- `helpers.py` – Common utilities (e.g., file reader, chunking).
- `summarizer.py` – Dedicated summarization agent logic.

---

### 🌐 `frontend/`

#### 📁 `components/`
- `ChatWindow.jsx` – Renders Q&A conversation.
- `UploadBox.jsx` – File upload UI.
- `AgentSelector.jsx` – UI dropdown to select which agent to use.
- `Spinner.jsx` – Circular loading indicator.
- `ScrollToTop.jsx` – Floating button to scroll page to top.

#### 📁 `pages/`
- `Home.jsx` – Full UI page with upload and chat integrated.

#### Other:
- `App.jsx` – Main React app router.
- `index.js` – React DOM entrypoint.
- `tailwind.config.js` – Enables dark mode, animations.
- `tailwind.css` – Tailwind directives (@tailwind base/components/utilities).

---

### 📓 `notebooks/`
- `fine_tuning.ipynb` – Load dataset, run LoRA fine-tuning.
- `rag_eval.ipynb` – Evaluate retrieval performance.

---

### 📁 `data/`
- `documents/` – Uploaded files stored here.
- `vector_store/` – FAISS index & metadata.
- `fine_tune_dataset/` – Training JSONL files for LoRA.

---

## 🛠️ How to Run

### Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
uvicorn api.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🧠 Learning Outcomes from This Project

| Concept | How it's Used |
|--------|---------------|
| **RAG** | `retriever.py` + `embedder.py` + `vector_store.py` |
| **LLMOps** | `logger.py`, `monitor.py`, `model_tracker.py` |
| **Multi-Agent** | `multi_agent_executor.py` dynamically invokes agent logic |
| **LangChain** | Modular chains in `base_agent.py` / `summarizer.py` |
| **Fine-Tuning** | `fine_tuning.ipynb` via LoRA method |
| **OpenAI API** | Used in `openai_client.py` for completions |
| **Frontend UX** | Dark/light themes, loading spinners, FAB scroll-to-top, animated UI |

---

## ✅ Final Note

This project gives you hands-on exposure to **real-world LLM system architecture**, combining:
- Embeddings + search
- Agent-based orchestration
- Fine-tuning
- API integration
- DevOps-style tracking

You're learning **everything needed to build production-level AI assistants.**


---

## 📘 What You Learn from This Project (In-Depth)

This project is structured to help you **master real-world LLM system design**. Here’s how each concept is implemented, what files are involved, and what exactly you learn:

---

### 🔹 1. Retrieval-Augmented Generation (RAG)

**Purpose**: Combine document retrieval with LLM reasoning.

**You Implemented**:
- `embedder.py`: Converts chunks into embeddings using `SentenceTransformer`
- `vector_store.py`: Saves/loads/searches via FAISS
- `retriever.py`: Pulls top-k matching chunks based on user queries
- `response_generator.py`: Feeds retrieved context to the LLM

**You Learned**:
- Chunking & semantic embedding
- How to use FAISS for fast vector search
- How retrieval improves LLM accuracy

---

### 🔹 2. Multi-Agent AI System

**Purpose**: Use specialized agents for different tasks (like summarization, QA, evaluation).

**You Implemented**:
- `base_agent.py`: Template for agent behavior
- `multi_agent_executor.py`: Selects the appropriate agent
- `summarizer.py`: One of the custom agents
- `AgentSelector.jsx`: Let users choose an agent from UI

**You Learned**:
- Modularity via agents
- Dynamic routing of requests to agents
- Real-world orchestration of AI behaviors

---

### 🔹 3. LLMOps

**Purpose**: Operational best practices for managing LLM systems.

**You Implemented**:
- `logger.py`: Logs all actions (query, upload, results)
- `monitor.py`: Tracks performance, usage
- `model_tracker.py`: Manages fine-tuned model versions

**You Learned**:
- Why tracking matters
- How to apply observability to LLM systems

---

### 🔹 4. Fine-Tuning with LoRA

**Purpose**: Efficient model fine-tuning without needing full retraining.

**You Implemented**:
- `fine_tuning.ipynb`: Notebook to fine-tune with LoRA
- `fine_tuned_model.py`: Loads fine-tuned model for live use
- `model_tracker.py`: Keeps metadata of fine-tuned runs

**You Learned**:
- Fine-tuning steps and dataset prep
- What LoRA is and how it saves GPU/compute
- How to integrate your tuned model into the app

---

### 🔹 5. LangChain

**Purpose**: Modular chains and tools for building LLM applications.

**You Used**:
- `LLMChain`, `PromptTemplate`, `RetrievalQA` in `base_agent.py` and `summarizer.py`

**You Learned**:
- LangChain patterns and benefits
- How to build chains manually to understand LangChain’s abstraction

---

### 🔹 6. OpenAI API Integration

**Purpose**: Send prompts and context to models like GPT-4.

**You Implemented**:
- `openai_client.py`: Central OpenAI wrapper
- `response_generator.py`: Sends prompt + context for completions

**You Learned**:
- Prompt design and templating
- Secure API usage via `.env`

---

### 🔹 7. Frontend System with Tailwind + React

**Purpose**: Build responsive, beautiful interfaces for AI apps.

**You Implemented**:
- `UploadBox.jsx`, `ChatWindow.jsx`, `AgentSelector.jsx`: Functional components
- `tailwind.css`, `tailwind.config.js`: Custom UI theme
- `ScrollToTop.jsx`, `Spinner.jsx`: Enhanced UX

**You Learned**:
- Dark/light theme setup
- Floating buttons and animated UI
- Best practices in clean React component design

---

## 🔄 End-to-End Workflow

1. Upload → Process → Embed
2. Query → Retrieve → Generate response
3. Agents execute specific logic
4. Monitoring & tracking log everything
5. Fine-tuned models can be plugged in
6. Frontend shows all activity beautifully

You now understand **how to go from theory to deployment** in real LLM apps.

