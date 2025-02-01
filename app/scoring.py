import nltk 
from language_tool_python import LanguageTool

nltk.download("punkt")
tool = LanguageTool('en-US')

def evaluate_response(text):
     # Fluency: Measure pauses and response length
    words = nltk.word_tokenize(text)
    fluency_score = len(words) / 10

     # Grammar: Check for errors
    grammar_errors = len(tool.check(text))
    grammar_score = max(0, 10 - grammar_errors)

     # Vocabulary: Count unique words
    unique_words = set(words)
    vocabulary_score = len(unique_words) / len(words) * 10