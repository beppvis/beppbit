import voiceRecognizer
import VoiceOutput
import datetime
import wikipedia
import webbrowser
states = [1,2,3]
state = 1
Micmode = False 

u_starting = "/// "
b_starting = ">>> "


def voiceInput(prompt:str,MicMode:bool):
    if MicMode:
        v_i = voiceRecognizer.get_input(2,prompt)
        v_i = str(v_i).lower()
    else:
        v_i = input(u_starting + prompt+" : ")
        v_i = v_i.lower()
    return v_i

def state_exec(state:int,voiceIn:str):
    if state == 1:
        VoiceOutput.voiceAudioOut("Hello there what is your name ?")
        name = voiceInput("Hello there what is your name ?",False)
        print(b_starting+"Hello "+name)
        VoiceOutput.voiceAudioOut("Hello " + name)
    elif state == 2:
        VoiceOutput.voiceAudioOut("Try saying what is the time beppbit ?")
    elif state == 3:
        VoiceOutput.voiceAudioOut("Hello there I am beppbit, A voice assistant")
        VoiceOutput.voiceAudioOut("Try asking what time is it?")
    elif state == 4:
        hour = str(datetime.datetime.now().hour)
        minute = str(datetime.datetime.now().minute)
        VoiceOutput.voiceAudioOut("It is currently "+minute+" minutes past "+hour)
    elif state == 5:
        VoiceOutput.voiceAudioOut("Searching Wikipedia...")
        voiceIn = voiceIn.replace("wikipedia","")
        result = wikipedia.summary(voiceIn,sentences = 2)
        VoiceOutput.voiceAudioOut(result)
    elif state == 6:
        webbrowser.open("youtube.com")
        VoiceOutput.voiceAudioOut("Opened Youtube")
    elif state == 7:
        webbrowser.open("google.com")
        VoiceOutput.voiceAudioOut("Opened Google")


while True:
    voice_in = voiceInput(b_starting,Micmode)
    if "what can you do" in voice_in:
        state_exec(2,voice_in)
        continue
    elif "hello" in voice_in:
        state_exec(1,voice_in)
        continue
    elif "intro" in voice_in:
        state_exec(3,voice_in)
    elif "time" in voice_in:
        state_exec(4,voice_in)
    elif "wikipedia" in voice_in or "wiki" in voice_in:
        state_exec(5,voice_in)
    elif "youtube" in voice_in:
        state_exec(6,voice_in)




