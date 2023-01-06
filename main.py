import voiceRecognizer
import VoiceOutput

VInput = str(voiceRecognizer.get_input(2))
VoiceOutput.voiceAudioOut(VInput)