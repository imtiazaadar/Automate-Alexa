import os
from datetime import datetime
import speech_recognition as speech_engine
import pyttsx3 as text_to_speech
from time import sleep
##
# Author : Imtiaz Adar
# Project : Time And Date By Alexa
# Language : Python
##
class alexa_time_date:
    def __init__(self):
        self.tts_engine = text_to_speech.init()
        self.voices = self.tts_engine.getProperty('voices')
        self.tts_engine.setProperty('voice', self.voices[1].id)

    def listen_command(self):
        listener = speech_engine.Recognizer()
        with speech_engine.Microphone() as mic:
            print('Listening...')
            listener.adjust_for_ambient_noise(mic)
            voice_of_mine = listener.listen(mic)
            try:
                command = listener.recognize_google(voice_of_mine).lower()
                print(f'Command of Imtiaz Adar : {command}')
                if 'alexa' in command:
                    if 'time' in command:
                        print('Telling the time')
                        self.talk('Telling the time')
                        time_now = self.tell_time()
                        formatted_time = f'Current time is : {time_now}'
                        print(formatted_time)
                        self.talk(formatted_time)
                        sleep(1)
                        self.talk('Thank You')

                    elif 'date' in command:
                        print('Telling the date')
                        self.talk('Telling the date')
                        date_now = self.tell_date()
                        formatted_date = f"Today's date is : {date_now}"
                        print(formatted_date)
                        self.talk(formatted_date)
                        sleep(1)
                        self.talk('Thank You')

            except Exception:
                print('Error !')

    def tell_time(self):
        time = datetime.now().strftime("%I:%M %p")
        return time

    def tell_date(self):
        date = datetime.now().strftime("%d %B %Y - %A")
        return date

    def talk(self, command):
        self.tts_engine.say(command)
        self.tts_engine.runAndWait()
        self.tts_engine.stop()

if __name__ == "__main__":
    time_date_class = alexa_time_date()
    time_date_class.listen_command()
    os.system('pause')