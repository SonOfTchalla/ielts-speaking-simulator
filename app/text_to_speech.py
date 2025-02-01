import pyttsx3

# text to speech conversion function
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()