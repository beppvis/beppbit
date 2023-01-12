import voiceRecognizer
import VoiceOutput

u_starting = "/// "

def voiceInput(prompt:str,MicMode:bool):
    if MicMode:
        v_i = voiceRecognizer.get_input(2,prompt)
    else:
        v_i = input(u_starting + prompt)
    return v_i


