
import pyttsx3

b_starting = ">>> "
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('rate',150)
engine.setProperty('voice',voice[0].id)
import os
from playsound import playsound

language = 'en'

def voiceAudioOut(prompt):
    prompt = str(prompt)
    engine.say(prompt)
    engine.runAndWait()
    print(b_starting+prompt)

def FaceOut(string:str):
    if len(string)%2 == 0:
        pass
    else:
        pass