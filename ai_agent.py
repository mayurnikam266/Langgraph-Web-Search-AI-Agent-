import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from typing import List
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
#from dotenv import load_dotenv
#load_dotenv() 
from langchain_core.messages import AIMessage, HumanMessage 



# System prompt
system_prompt = "Act as an AI chatbot which is smart and friendly"

# Create agent and get response from model
def get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider,api_key_model,tavily_api_key):
  
  if not api_key_model:
        raise ValueError("Missing Model API Key")
  if provider == "groq":
    os.environ["GROQ_API_KEY"] = api_key_model  # ✅ Set the required env var
    model_llm = ChatGroq(model=llm_id)

  elif provider == "openai":
    model_llm = ChatOpenAI(model=llm_id, api_key=api_key_model)
  else:
      raise ValueError("Unsupported provider. Use 'groq' or 'openai'.")

  
  
  
  tools = []
  if allow_search and tavily_api_key:
    tavily_search = TavilySearch(tavily_api_key=tavily_api_key)
    tools.append(tavily_search)
  ## agent calling 
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
