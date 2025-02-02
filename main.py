import os
from gtts import gTTS


import pyttsx3
"""
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("voice.mp3")
    os.system("voice.mp3")



if __name__ == '__main__':
    print("Welcome to Robospeacker")
    x = input("Enter the command: ")
    speak(x)

"""
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to Robospeacker")
    while True:
        x = input("Enter the command: ")
        if x == "exit":
            speak("Thank you for using Robospeacker")
            break
        speak(x)


