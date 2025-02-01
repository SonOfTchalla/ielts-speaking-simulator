from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer


# Load pre-trained conversational model (DialoGPT)
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create a text-generation pipeline
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Response generation function
def generate_response(user_input):
    response = chatbot(user_input)[0]["generated_text"]
    return response