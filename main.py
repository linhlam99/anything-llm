# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
memory = []  # This will store the conversation

class Prompt(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Hello, Anything-LLM!"}

@app.post("/chat")
def chat(prompt: Prompt):
    # Save prompt to memory
    memory.append(f"User: {prompt.text}")
    
    # For now, our "model" just echoes the last message
    response = f"Anything-LLM reply to: {prompt.text}"
    memory.append(f"LLM: {response}")
    
    return {"response": response, "conversation": memory}
import requests

url = "http://192.168.2.25:7860/chat"
data = {"text": "Hello LLM, how are you?"}

response = requests.post(url, json=data)
print(response.json())
