from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import wikipedia
import wolframalpha
import os
import speech_recognition as sr
import smtplib
from googletrans import Translator
import speak

translator = Translator()
r = sr.Recognizer()

def get_lyrics(singer, song):
    singer = singer.lower()
    singer = "".join(singer.split())
    song = song.lower()
    song = "".join(song.split())
    url = 'https://www.azlyrics.com/lyrics/'+singer+'/'+song+'.html'
    data = urllib.request.urlopen(url)
    data2 = data.read()
    raw = BeautifulSoup(data2,'html.parser')
    lyr = raw.find_all("div", attrs={"class": None, "id": None})
    lyrics = [i.getText() for i in lyr]
    return lyrics

def write_infile(lyrics,singer,song):
    f = open(singer+"_"+song+".txt", 'w')
    f.write("\n".join(lyrics).strip())
    f.close()

def details_input():
    lang = 'en'
    print("Tell me the singer")
    speak.tts('Tell me the singer', lang)
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    
    singer = text

    print("Tell me the name of the song")
    speak.tts('Tell me the name of the song', lang)
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    song = text
    lyrics = get_lyrics(singer,song)
    write_infile(lyrics,singer,song)
    return [singer,song]

def detail_input():
    lang ='hi'
    print("गायक का नाम बताएं")
    speak.tts('गायक का नाम बताएं', lang)
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    
    singer = text

    print("गाने का नाम बताएं")
    speak.tts('गाने का नाम बताएं', lang)
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    song = text
    lyrics = get_lyrics(singer,song)
    write_infile(lyrics,singer,song)
    return [singer,song]
