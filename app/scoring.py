import nltk 
from language_tool_python import LanguageTool

nltk.download("punkt")
tool = LanguageTool('en-US')

def evaluate_response(text):
    