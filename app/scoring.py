import nltk 
from language_tool_python import LanguageTool

nltk.download("punkt")
tool = LanguageTool('en-US')

def evaluate_response(text):
     # Fluency: Measure pauses and response length
    words = nltk.word_tokenize(text)
    fluency_score = len(words) / 10