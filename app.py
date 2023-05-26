from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Pretrained model name
PRETRAINED_MODEL_NAME = "gpt2"

# Initialize tokenizer
tokenizer = GPT2Tokenizer.from_pretrained(PRETRAINED_MODEL_NAME)

# Initialize model
model = GPT2LMHeadModel.from_pretrained(PRETRAINED_MODEL_NAME)

# Load state dictionary from pickle file
model.load_state_dict(torch.load("pytorch_model.bin"))

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate/")
async def generate_text(input: InputText):
    # Preprocess text input
    input_ids = tokenizer.encode(input.text, return_tensors="pt")
    
    # Generate text
    # You may want to adjust parameters here for text generation
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, temperature=0.7)

    # Decode generated text
    generated_text = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    return {"generated_text": generated_text}

