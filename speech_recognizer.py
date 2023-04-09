#!/usr/bin/env python3
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import configparser

config = configparser.ConfigParser()
config.read('.config')

open_api_key = config.get('open_api_key', 'key')

def speech_recognition():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Whisper API
    try:
        ai_reply = r.recognize_whisper_api(audio, api_key=open_api_key)
        print("Whisper API thinks you said" + ai_reply)
        return ai_reply
    except sr.RequestError as e:
        print("Could not request results from Whisper API")
        return -1


if __name__ == "__main__":
    speech_recognition()
