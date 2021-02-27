import speech_recognition as sr
import sys
import time
import os

from os import path
location = sys.stdin.readlines()[0].replace('"', '')

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)) + "/voicedata", location)


r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file



# recognize speech using google
print(r.recognize_google(audio))