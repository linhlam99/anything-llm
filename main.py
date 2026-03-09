# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Anything-LLM Test API")

# Example request/response model
class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Hello, Anything-LLM!"}

@app.post("/generate")
def generate_text(request: PromptRequest):
    # For now, just echo back the prompt
    return {"prompt": request.prompt, "response": f"You said: {request.prompt}"}
