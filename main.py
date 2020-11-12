import speech_recognition as sr
import time
from time import ctime
import webbrowser
import playsound
import random
import os
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

# To set the voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function for text to speech using pyttsx3
def luna_speak(audio_string):
    engine.say(audio_string)
    engine.runAndWait()
    print(audio_string)
    
# Function to recognize speech
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            luna_speak(ask)
        audio= r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            luna_speak('Sorry! I did not get that')
        except sr.RequestError:
            luna_speak('Sorry, my speech service is down')
        return voice_data

#Set of question promts (More features to be added soon!)
def respond(voice_data):
    if 'what is your name' in voice_data:
        luna_speak('My name is Luna')
    if 'what time is it' in voice_data:
        luna_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        luna_speak('Here is what I found for you')
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/'+location+'/&amp'
        webbrowser.get().open(url)
        luna_speak('Here is the location'+ location)
    if 'exit' in voice_data:
        luna_speak('Bye')
        exit()

# Loop for continued listening 
time.sleep(1)
luna_speak('Hello! How can I help you?')
while 1:
    voice_data=record_audio()
    respond(voice_data)

