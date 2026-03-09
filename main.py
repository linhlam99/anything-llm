# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI(title="Anything-LLM API")

# Load model and tokenizer (small model for testing)
MODEL_NAME = "EleutherAI/gpt-neo-125M"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 50

@app.post("/generate")
def generate_text(request: PromptRequest):
    inputs = tokenizer(request.prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=request.max_length)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"prompt": request.prompt, "response": text}
