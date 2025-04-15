import pyttsx3

def text_to_speech(text):
    """Converts given text to speech."""
    if text.strip():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
