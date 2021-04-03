import cv2
import numpy as np
from matplotlib import pyplot as plt
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
r = konus.Recognizer()
with konus.Microphone() as source:
    speak("ne yapmamı istersin murat?")
    audio = r.listen(source)
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

def tanımlama():
	while(True):
		a=0
		
		faces_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


		video=cv2.VideoCapture(0)
		i=0
		while(True):
			_,kare=video.read()
	
	
			gray=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
			faces=faces_cascade.detectMultiScale(gray,1.1,4)
 	
			for (x,y,w,h) in faces :
				cv2.rectangle(kare,(x,y), (x+w,y+h),(0,255,0),3)
				i=1+i
				if i==2:
					a=a+1
					speak("yüzün algılandı,nasılsın")
					
		 	 			
			cv2.imshow("MAA YÜZ TANIMA SİSTEMİ",kare)	

			if cv2.waitKey(1) & 0xFF == ord("k") :
       		         break
	
		


		video.release()
		cv2.destroyAllWindows()		
    


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
    if text == "yüz tanımla":
       komut(tanımlama())    
