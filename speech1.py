import speech_recognition as speech_recog

mic = speech_recog.Microphone()
recog = speech_recog.Recognizer()

with mic as audio_file:
    print("silakan bicara:")
    
    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)
    print("Kamu berkata: " + recog.recognize_google(audio, language="en-GB"))