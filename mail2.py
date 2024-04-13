import speech_recognition as sr
from googletrans import Translator
import smtplib
import urllib.request, urllib.error, urllib.parse
import speak

translator = Translator()
r = sr.Recognizer()

def email():
    lang = 'hi'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    speak.tts('किसको भेजना चाहते हैं', lang)
    r_add = input('किसको भेजना चाहते हैं:')
    server.login("sirji.beproject@gmail.com", "sirjibeproject")
    speak.tts('क्या ईमेल भेजना हैं', lang)
    with sr.Microphone() as source:
        audio = r.listen(source)
    txt = r.recognize_google(audio)
    tx=translator.translate(txt)
    if tx.src=='en':
        lang='en'
        speak.tts('Your message was', lang)
        print (txt)
        server.sendmail("sirji.beproject@gmail.com", r_add, txt.encode())
        server.quit()
        speak.tts('Email has been sent', lang)
    else:
        speak.tts('आपका संदेश था', lang)
        txt = r.recognize_google(audio,language='hi')
        print(txt)
        server.sendmail("sirji.beproject@gmail.com", r_add, txt.encode())
        server.quit()
        speak.tts('ईमेल भेजा जा चुका है', lang)
