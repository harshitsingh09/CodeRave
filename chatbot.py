import speech_recognition as sr
from googletrans import Translator
import speak
import nltk
from nltk.stem.lancaster import LancasterStemmer
import random

def chat():
    stemmer = LancasterStemmer()

    translator = Translator()
    r = sr.Recognizer()


    training_data = []
    training_data.append({"class":"greeting", "sentence":"hello how are you?"})
    training_data.append({"class":"greeting", "sentence":"how is your day?"})
    training_data.append({"class":"greeting", "sentence":"good day"})
    training_data.append({"class":"greeting", "sentence":"how is it going today?"})
    training_data.append({"class":"greeting", "sentence":"What is up?"})
    training_data.append({"class":"greeting", "sentence":"Hi friends"})
    training_data.append({"class":"greeting", "sentence":"good morning"})
    training_data.append({"class":"greeting", "sentence":"good evening"})


    training_data.append({"class":"goodbye", "sentence":"have a nice day"})
    training_data.append({"class":"goodbye", "sentence":"see you later"})
    training_data.append({"class":"goodbye", "sentence":"have a nice day"})
    training_data.append({"class":"goodbye", "sentence":"talk to you soon"})
    training_data.append({"class":"goodbye", "sentence":"good bye"})
    training_data.append({"class":"goodbye", "sentence":"goodbye"})
    training_data.append({"class":"goodbye", "sentence":"nice to meet you"})

    training_data.append({"class":"food", "sentence":"make me a sandwich"})
    training_data.append({"class":"food", "sentence":"can you make a tasty dish?"})
    training_data.append({"class":"food", "sentence":"having a lunch today?"})
    training_data.append({"class":"food", "sentence":"what's for breakfast?"})
    training_data.append({"class":"food", "sentence":"I am hungry"})
    training_data.append({"class":"food", "sentence":"Want food"})
    training_data.append({"class":"food", "sentence":"Let us have lunch"})
    training_data.append({"class":"food", "sentence":"Apples are healthy"})

    training_data.append({"class":"football", "sentence":"football is my favourite sport"})
    training_data.append({"class":"football", "sentence":"That was an amazing goal by the defender"})
    training_data.append({"class":"football", "sentence":"goal keepers can join strikers too"})
    training_data.append({"class":"football", "sentence":"That header was on mark"})
    training_data.append({"class":"football", "sentence":"shoot the ball"})
    training_data.append({"class":"football", "sentence":"juicy half-volley"})
    training_data.append({"class":"football", "sentence":"swing the ball from the corner"})
    
    training_data.append({"class":"emotions", "sentence":"are you sad?"})
    training_data.append({"class":"emotions", "sentence":"you don't look happy"})
    training_data.append({"class":"emotions", "sentence":"what is the reason of your gloomy face"})
    training_data.append({"class":"emotions", "sentence":"Not feeling well?"})
    training_data.append({"class":"emotions", "sentence":"Love is in the air"})
    training_data.append({"class":"emotions", "sentence":"anger leads to suffering, suffering leads to pain, pain leads to the dark side"})
    training_data.append({"class":"emotions", "sentence":"Control your emotions. Don't let them betray you"})
    training_data.append({"class":"emotions", "sentence":"I am angry"})
    
    greeting=["how are you","Hello","Good day pal"]
    goodbye=["see you soon", "Bye","have a nice day"]
    food=["I am very hungry", "I would love to eat something", "Burgers are my favourite", "food is amazing"]
    football=["Oh football, did you see the match last night? How amazing was that?", "sports always gets me pumped up", "football really is a great sport"]
    emotions=["Talk about some strong emotions", "hmmm... difficult it is to understand emotions", "Always stay happy no matter what"]


    corpus_words = {}
    class_words = {}

    classes = list(set([a['class'] for a in training_data]))
    for c in classes:
       
        class_words[c] = []


    for data in training_data:
        
        for word in nltk.word_tokenize(data['sentence']):
            
            if word not in ["?", "'s"]:
               
                stemmed_word = stemmer.stem(word.lower())
               
                if stemmed_word not in corpus_words:
                    corpus_words[stemmed_word] = 1
                else:
                    corpus_words[stemmed_word] += 1

                
                class_words[data['class']].extend([stemmed_word])


    def calculate_class_score(sentence, class_name, show_details=True):
        score = 0
       
        for word in nltk.word_tokenize(sentence):
            
            if stemmer.stem(word.lower()) in class_words[class_name]:
                
                score += (1 / corpus_words[stemmer.stem(word.lower())])
                
        return score

    lang = 'en'

    speak.tts('Start conversation', lang)
    print('Start conversation: ')
    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)
            print ('Done!')
        sentence = r.recognize_google(audio)
        tx=translator.translate(sentence)
        high=0
        if tx.src=='en':
            print ('You: '+sentence)
            for c in class_words.keys():
                score=calculate_class_score(sentence, c)
                if score>high:
                    high=score
                    high_class=c
            if high==0:
                print('Vani: I did not get you')
                speak.tts('I did not get you',lang)
                break
            if high_class=="greeting":
                a = random.choice(greeting)
                print('Vani: '+a)
                speak.tts(a,lang)
            elif high_class=="goodbye":
                a = random.choice(goodbye)
                print('Vani: '+a)
                speak.tts(a,lang)
            elif high_class=="food":
                a = random.choice(food)
                print('Vani: '+a)
                speak.tts(a,lang)
            elif high_class=="football":
                a = random.choice(football)
                print('Vani: '+a)
                speak.tts(a,lang)
            elif high_class=="emotions":
                a = random.choice(emotions)
                print('Vani: '+a)
                speak.tts(a,lang)
        else:
            lang='hi'
            sentence = r.recognize_google(audio, language='hi')
            print ('आप: '+sentence)
            sent_hi=translator.translate(sentence, dest='en')
            send=(sent_hi.text)
            for c in class_words.keys():
                score=calculate_class_score(send, c)
                if score>high:
                    high=score
                    high_class=c        
            if high==0: 
                lang='hi'
                print('सर-जी: आपको समझ नहीं सका')
                speak.tts('आपको समझ नहीं सका',lang)
                break
            else:
                if high_class=="greeting":
                    a = random.choice(greeting)
                    b = translator.translate(a, dest='hi')
                    print("सर-जी: " + b.text)
                    speak.tts(b.text,lang)
                elif high_class=="goodbye":
                    a = random.choice(goodbye)
                    b = translator.translate(a, dest='hi')
                    print("सर-जी: " + b.text)
                    speak.tts(b.text,lang)
                elif high_class=="food":
                    a = random.choice(food)
                    b = translator.translate(a, dest='hi')
                    print("सर-जी: " + b.text)
                    speak.tts(b.text,lang)
                elif high_class=="emotions":
                    a = random.choice(emotions)
                    b = translator.translate(a, dest='hi')
                    print("सर-जी: " + b.text)
                    speak.tts(b.text,lang)
                
    



