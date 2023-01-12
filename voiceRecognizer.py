import speech_recognition as sr
recording = sr.Recognizer()
starting = "/// "
def get_input(device_index_1:int,prompt:str):
    with sr.Microphone(device_index=device_index_1) as source:
        recording.adjust_for_ambient_noise(source)
        print(starting + prompt)
        audio = recording.listen(source)
        audio = recording.recognize_google(audio)
        print("You can stop")
        return audio
