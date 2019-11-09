#!/usr/bin/env python3

import speech_recognition as sr
from datetime import datetime, timedelta

while True:
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        method = input("Speech Recognition Engine: ")
        print("Listening...")
        audio = recognizer.listen(source)
        if method == "Google":
            try:
                time_a = datetime.now()
                transcribed_text = recognizer.recognize_google(audio)
                print(transcribed_text)
                time_b = datetime.now()
                time_c = time_b - time_a
                time_difference = time_c.seconds + time_c.microseconds / 1E6
                print(time_difference)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        if method == "Wit":
            try:
                WIT_KEY = "KUXXHOKXUXGSJODWSEK3RPV6CDBSQBUV"
                time_a = datetime.now()
                transcribed_text = recognizer.recognize_wit(audio, key=WIT_KEY)
                print(transcribed_text)
                time_b = datetime.now()
                time_c = time_b - time_a
                time_difference = time_c.seconds + time_c.microseconds / 1E6
                print(time_difference)
            except sr.UnknownValueError:
                print("Wix Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Wit Speech Recognition service; {0}".format(e))
