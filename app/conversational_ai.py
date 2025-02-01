from transformers import pipeline

# Load pre-trained conversational model
chatbot = pipeline("conversational")

# Response generation function
def generate_response(user_input):
    response = chatbot(user_input)[0]["generated_text"]
    return response