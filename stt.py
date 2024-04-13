import speech_recognition as sr
from googletrans import Translator

def speech():
    translator = Translator()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print ('How may I help you?')
        audio = r.listen(source)
        print ('Okay')
 
    text = r.recognize_google(audio)
    tx = translator.translate(text)
    return (text)



