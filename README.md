# Speech-Assistant
A python speech assistant called Luna that uses speech recognition and text-to-speech. It recognizes the commands and then takes appropriate actions. Currently, users can search the internet and ask Luna a bunch of questions about itself. Users can also look up a location on Google maps.
Fun fact: It is named Luna after my laptop :D

# Motivation
I wanted to write a script that would help me quickly search for things while I am coding instead of me going back and forth between a browser and my IDE. While working on the application, I decided to add more functionality so that I don't have to manually type my search. Initially, all Luna did was search the browser but slowly, it's getting more functionality.

# Installation (for windows)
```
  cd .venv/Scripts       
  Activate
  cd ../..
  pip install -r requirements.txt
  python main.py
```

# Issues with gTTs
Initially, the application was using Google text to speech. However, the response time was a little slow because of the internet requirements of gTTS so I unistalled it and instead used pyttsx3, an offline cross-platform Text-to-Speech library.

# Future updates
I would like to add functionality to send emails and check google calenders. Also, perhaps a way to tell jokes! :)
