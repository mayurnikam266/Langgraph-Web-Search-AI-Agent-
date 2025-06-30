import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from typing import List
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
#from dotenv import load_dotenv
#load_dotenv() 
from frontend import API_KEY_MODEL,API_KEY_TAVILY
from langchain_core.messages import AIMessage, HumanMessage 


# Load API keys from environment variables
groq_llm = ChatGroq(model="llama3-70b-8192", api_key=API_KEY_MODEL)



TAVILY_API_KEY = API_KEY_TAVILY




# Initialize search tool
tavily_search = TavilySearch(api_key=TAVILY_API_KEY)

# System prompt
system_prompt = "Act as an AI chatbot which is smart and friendly"

# Create agent and get response from model
def get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):
  if provider == "groq":
    model_llm = ChatGroq(model=llm_id, api_key=os.getenv("GROQ_API_KEY"))
  elif provider == "openai":
    model_llm = ChatOpenAI(model=llm_id, api_key=OPENAI_API_KEY)
  else:
      raise ValueError("Unsupported provider. Use 'groq' or 'openai'.")

  
  tools=[tavily_search] if allow_search else []
  agent = create_react_agent(
      model=model_llm,
      tools=tools,
      prompt=system_prompt
)

# Ask a question

  state = {"messages":query}

# Get response
  response = agent.invoke(state)
  messages=response.get("messages")
  ai_message=[message.content for message in messages if isinstance(message,AIMessage)]
  return ai_message[-1]
