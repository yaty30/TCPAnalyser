import pyttsx3
from utils import counter, addCount, alterCSV, patch_say
import pandas as pd
from playsound import playsound
import time

engine = pyttsx3.init()


def Say(word):
    addCount()
    engine.say(word)
    engine.runAndWait()


def say(word):
    print(word)
    val = None
    if word == "Good Morning":
        val = "gm"
    elif word == "Good Afternoon":
        val = "ga"
    elif word == "YES":
        val = "yes"
    elif word == "NO":
        val = "no"

    audio = patch_say(val)
    playsound(audio)


def TTS(word):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[17].id)
    # setVolumn(0.25)
    if counter() == 0:
        say(word)
    else:
        engine.endLoop()
        engine.stop()

        say(word)

    return "ok"


def DefaultTTS(data):
    word = data["word"]

    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices')


    engine.setProperty('voice', voices[data["voiceID"]].id)
    engine.setProperty('rate', data["speechRate"])
    engine.setProperty('volume', data["volume"])

    engine.say(word)
    engine.runAndWait()

    time.sleep(2)
    engine.endLoop()

    return "ok"


def getVoices():
    voices = engine.getProperty('voices')

    voices_list = []
    for i, voice in enumerate(voices):
        voices_list.append({
            "id": i,
            "name": voice.id.split(".voice.", 1)[1].capitalize(),
            "gender": voice.gender.split("VoiceGender", 1)[1].lower()
        })

    return voices_list

def setVoice(index):
    # femael => voices[17].id
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[index].id)


def setSpeechRate(val):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + val)


def setVolumn(val):
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume - val)


def generateProfile():
    data = engine.getProperty()

    header = ["Speech Rate", "Voice", "Volume"]
    dataSet = [data.rate, data.voice, data.volume]

    alterCSV("profile.csv", header, dataSet)


def configuration(settings):
    setVoice(settings.voiceIndex)
    setSpeechRate(settings.speechRate)
    setVolumn(settings.volumn)

    return ""
