import wikipedia
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
query = "phone"
wikipedia.set_lang("hi")
results = wikipedia.summary(query)
print(results)
speak(results)
