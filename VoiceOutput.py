
from gtts import gTTS
import os
from playsound import playsound

language = 'en'

def voiceAudioOut(prompt):
    prompt = str(prompt)
    out = gTTS(text=prompt,lang=language,slow=False)
    out.save("{prompt}.mp3")
    playsound("{prompt}.mp3")

def FaceOut(string:str):
    if len(string)%2 == 0:
        pass
    else:
        pass