import speech_recognition as sr
from googletrans import Translator
import stt
import mail1
import mail2
import speak
import os
import song
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import smtplib
import wikipedia
import wolframalpha


def run():
    translator = Translator()
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print ('How may I help you?')
            audio = r.listen(source)
        #text = stt.speech()
        text = r.recognize_google(audio)
        tx=translator.translate(text)
        if tx.src=='en':
            print(tx.text)
            words = (tx.text).split()
            if "email" in words or "mail" in words or "e-mail" in words:
                if "send" in words or "forward" in words:
                    mail1.email()
            elif "open" in words:
                if "calculator" in words:
                    speak.tts('Opening calculator', lang)
                    os.system('calc.exe')
                elif "Notepad" in words:
                    speak.tts('Opening notepad', lang)
                    os.system('notepad.exe')
                elif "Word" in words:
                    speak.tts('Opening word', lang)
                    filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
                    os.system('start winword.exe'.format(filepath))
                elif "PowerPoint" in words or "PPT" in words:
                    speak.tts('Opening power point', lang)
                    filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
                    os.system('start powerpnt.exe'.format(filepath))
                elif "PDF" in words:
                    speak.tts('Opening PDF', lang)
                    filepath = "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
                    os.system('start AcroRd32.exe'.format(filepath))
                elif "onenote" in words:
                    speak.tts('Opening onenote', lang)
                    filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
                    os.system('start onenote.exe'.format(filepath))
                elif "Excel" in words:
                    speak.tts('Opening excel', lang)
                    filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
                    os.system('start excel.exe'.format(filepath))
            elif "lyrics" in words:
                s = song.details_input()
                print("\r\n")
                F = open(s[0]+"_"+s[1]+".txt",'r')
                ly=F.read()
                print(ly)
                F.close()
                os.remove(s[0]+"_"+s[1]+".txt")
            else:
                try:           
                    app_id = "3WPY8L-LUUR9EVXXK"
                    client = wolframalpha.Client(app_id)
                    res = client.query(tx.text)
                    answer = next(res.results).text
                    print(answer)
                except:
                    print(wikipedia.summary(tx.text, sentences=2))
        else:
            text = r.recognize_google(audio,language='hi')
            print(text)
            lang = 'hi'
            words = text.split()
            if "भेजो" in words or "भेजना" in words or "भेजिए" in words or "भेज" in words:
                if "ईमेल" in words or "मेल" in words:
                    mail2.email()
            elif "खोलें" in words or "खोलो" in words or "खोलिए" in words or "चालू" in words:
                if "कैलकुलेटर" in words or "कैल्कुलेटर" in words or "कैल्क्यूलेटर" in words:
                    speak.tts('कैलकुलेटर खोल दिया गया है', lang)
                    os.system('calc.exe')
                elif "नोटपैड" in words:
                    speak.tts('नोटपैड खोल दिया गया है', lang)
                    os.system('notepad.exe')
                elif "पावर" in words or "PPT" in words:
                    if "पॉइंट" in words:
                        speak.tts('पावर पॉइंट खोल दिया गया है', lang)
                        filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
                        os.system('start powerpnt.exe'.format(filepath))
                elif "वर्ड" in words:
                    speak.tts('वर्ड खोल दिया गया है', lang)
                    filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
                    os.system('start winword.exe'.format(filepath))
                elif "PDF" in words:
                    speak.tts('PDF खोल दिया गया है', lang)
                    filepath = "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
                    os.system('start AcroRd32.exe'.format(filepath))
                elif "नोट" in words:
                    if "1" in words:
                        speak.tts('वन् नोट खोल दिया गया है', lang)
                        filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
                        os.system('start onenote.exe'.format(filepath))
                elif "एक्सेल" in words or "XL" in words:
                    speak.tts('एक्सेल खोल दिया गया है', lang)
                    filepath = "C:\Program Files (x86)\Microsoft Office\root\Office16"
                    os.system('start excel.exe'.format(filepath))
            elif "लिरिक्स" in words:
                s = song.detail_input()
                print("\r\n")
                F = open(s[0]+"_"+s[1]+".txt",'r')
                ly=F.read()
                print(ly)
                F.close()
                os.remove(s[0]+"_"+s[1]+".txt")
            else:
                try:
                    tx=translator.translate(text, dest='en')
                    app_id = "3WPY8L-LUUR9EVXXK"
                    client = wolframalpha.Client(app_id)
                    res = client.query(tx.text)
                    answer = next(res.results).text
                    ans = translator.translate(answer, dest='hi')
                    print(ans.text)
                except:
                    wikipedia.set_lang('hi')
                    print(wikipedia.summary(text, sentences=2))
            
