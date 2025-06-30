from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent
from typing import Optional

class RequestState(BaseModel):
    model_name: Optional[str] = "llama3-70b-8192"
    model_provider: Optional[str] = "groq"
    system_prompt: str
    messages: str
    allow_search: Optional[bool] = True


app = FastAPI(title="langgraph AI Agent")
ALLOWED_MODEL_NAMES= ["llama3-70b-8192"]

@app.post("/chat")
def chat_endpoint(request : RequestState):
  """
  API endpoint to interact with the Chatbot using LangGraph and search tools.
  """
  if request.model_name not in    ALLOWED_MODEL_NAMES:
    return {"error": "Model not allowed. Please use a valid model name."}
  llm_id = request.model_name
  provider = request.model_provider 
  query=request.messages
  allow_search=request.allow_search 
  system_prompt = request.system_prompt
  
  response= get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider)
  return response

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="127.0.0.2", port=8000)
  