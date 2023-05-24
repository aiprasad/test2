from flask import Flask, request
from transformers import pipeline

app = Flask(__name__)

# Load the model
generate_text = pipeline(model="databricks/dolly-v2-3b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json['prompt']
    return generator(prompt, max_length=100, do_sample=True, temperature=0.9)
