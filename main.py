# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = FastAPI()

MODEL_NAME = "tiiuae/falcon-7b-instruct"  # Replace with Anything-LLM model
device = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto" if device=="cuda" else None)
model.eval()  # ensure evaluation mode
print("Model loaded!")

class Prompt(BaseModel):
    text: str
    max_length: int = 1000

@app.get("/")
def root():
    return {"message": "Hello, Anything-LLM!"}

@app.post("/generate")
def generate(prompt: Prompt):
    inputs = tokenizer(prompt.text, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=prompt.max_length)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": text}
