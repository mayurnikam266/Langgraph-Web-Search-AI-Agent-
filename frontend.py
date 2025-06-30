import streamlit as st 
import requests

st.set_page_config(page_title="LangGraph AI Agent",layout="centered",page_icon=":robot_face:")

st.title("AI chatbot Agent")
st.write("Create and Interact with AI Agents")

system_prompt=st.text_area("Define you AI Agent:",height=70, placeholder="Type your system prompt here ...")

MODEL_NAMES_GROQ = ["llama3-70b-8192"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select Model Provider:",("groq","openai"))

api_key_model= st.text_input("Enter your API Key of Selected Model ", type="password", placeholder="Enter your API Key here...").strip()
api_key_model = api_key_model if api_key_model else None
tavily_api_key = st.text_input("Enter your Tavily API Key To search n Web", type="password", placeholder="Enter your Tavily API Key here...")
tavily_api_key = tavily_api_key.strip() if tavily_api_key else None


if provider == "groq":
    model_name = st.selectbox("Select Model:", MODEL_NAMES_GROQ)
elif provider == "openai":
    model_name = st.selectbox("Select Model:", MODEL_NAMES_OPENAI)

allow_search =st.checkbox("Allow Web Search")
user_query = st.text_area("Ask a question to your AI Agent:",height=70, placeholder="Ask Anything ...")

API_URL ="http://localhost:8000/chat"
if st.button("Ask AI AGENT"):
    if user_query.strip():
        payload={
            "model_name": model_name,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": user_query,
            "allow_search": allow_search,
            "api_key_model": api_key_model,
            "tavily_api_key": tavily_api_key
        }
        response = requests.post(API_URL, json=payload)

        try:
            response_data = response.json()
            if response.status_code == 200:
                if isinstance(response_data, dict) and "error" in response_data:
                    st.error(response_data["error"])
                else:
                    st.success("AI Agent Response:")
                    st.markdown(response_data)
            else:
                st.error(f"Server error {response.status_code}")
                st.write(response_data)
        except Exception as e:
            st.error("Invalid response from server.")
            st.write(response.text)  # This shows the raw text from server


        