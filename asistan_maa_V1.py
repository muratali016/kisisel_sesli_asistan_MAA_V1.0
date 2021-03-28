import  webbrowser
import speech_recognition as konus
from os import system as komut
import os
import random
from playsound import playsound
from gtts import gTTS  

def speak(string):
    tts=gTTS(string ,lang='tr')
    rand =random.randint(1,10000)
    file='audio-'+str (rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


buyukAlfabe = "ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe ="abcçdefgğhiıjklmnoöprsştuüvyz"

def lower(text:str):
    neWText = str()
    for i in text:
        if i in buyukAlfabe:
            index = buyukAlfabe.index(i)
            neWText += kucukAlfabe[index]
        else:
            neWText += i


    return  neWText


r = konus.Recognizer()
with konus.Microphone() as source:
    
    speak("Ne yapmamı istersin?")
    audio = r.listen(source)





Flag = str

try:
    text = r.recognize_google(audio,language="tr-TR")
    speak("Algılanan :" + text)
    Flag = True
    text = lower(text)
except konus.UnknownValueError:
    speak("Ne dedin bir daha dene?")
except konus.RequestError as e:
    speak("sistem sıkıntılı; {0}".format(e))

if Flag:
    if text == "ilk kelime listesini aç":
       komut(webbrowser.get().open('https://docs.google.com/document/d/1TzZ6WNTOlYPrn2viliSSUNuws5nQ966KCVMMoy4SNx4/edit') )
if Flag:
    if text =="ikinci kelime listesi":
        komut("henüz daha eklenmedi")
if Flag:
    if text =="sınıfa geç":
       komut(webbrowser.get().open('https://classroom.google.com/u/0/c/MjgwNDczNTQzMDIz') )
       

