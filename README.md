# 🤖 LangGraph Web Search AI Agent

LangGraph AI Agent is a conversational web-based chatbot powered by FastAPI (backend) and Streamlit (frontend). It allows users to interact with powerful LLMs like **Groq's LLaMA 3** and **OpenAI GPT-4o-mini**, with optional web search capability using the **Tavily API**.

---

## 🧠 Features

- 🌐 Choose between **Groq** or **OpenAI** models.
- ✍️ Define custom system prompts to guide agent behavior.
- 🔍 Enable or disable web search (Tavily integration).
- ⚙️ Unified Dockerized deployment for easy scaling.
- 📤 RESTful API via FastAPI + interactive frontend via Streamlit.

---

## 🚀 Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| 🧠 Backend    | FastAPI        |
| 🧑‍💻 Frontend  | Streamlit      |
| 🤖 Models     | Groq LLaMA 3 / OpenAI GPT-4o-mini |
| 🌍 Web Search | Tavily API     |
| 📦 Docker     | Containerization |
| ☁️ Cloud      | AWS ECS / Lambda / EC2 |

## 🐳 Docker Usage

### ✅ Step 1: Build the Docker Image

```bash
# Clone the repository and navigate into the project directory
git clone https://github.com/yourusername/langgraph-ai-agent.git
cd langgraph-ai-agent

# Build the Docker image with a custom tag
docker build -t ai-agent-app .

