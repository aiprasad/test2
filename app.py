import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from fastapi import FastAPI

app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-3b")
model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-3b")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate/")
def generate_text(prompt: str):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"prompt": prompt, "generated_text": generated_text}

