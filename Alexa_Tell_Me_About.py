from os import system
import speech_recognition as speech_engine
import pyttsx3 as tts_engine
import wikipedia as wiki
from time import sleep
from word2number import w2n
##
# Author : Imtiaz Adar
# Project : Alexa Tell About
# Language : Python
##
class alexa_tell_me_about:
    def __init__(self):
        self.voice_engine = tts_engine.init()
        self.voices = self.voice_engine.getProperty('voices')
        self.voice_engine.setProperty('voice', self.voices[1].id)

    def listen(self):
        listener = speech_engine.Recognizer()
        with speech_engine.Microphone() as mic:
            print('Listening...')
            listener.adjust_for_ambient_noise(mic)
            my_voice = listener.listen(mic)
            try:
                command = listener.recognize_google(my_voice).lower()
                print(f'Command of Imtiaz Adar : {command}')
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    if 'tell me about' in command:
                        command = command.replace('tell me about', '')
                        print('Telling you...')
                        self.talk('Telling you')
                        self.talk('How many lines do you want to hear ? ')
                        listener.adjust_for_ambient_noise(mic)
                        lines = listener.listen(mic)
                        try:
                            line_command = listener.recognize_google(lines).lower()
                            line_command = line_command.split(' ')
                            num_of_sen = w2n.word_to_num(line_command[0])
                            print(f'{num_of_sen} lines')
                            self.talk(f'{num_of_sen} lines, okay commandsir!')
                            self.tell_about(command, int(num_of_sen))
                            sleep(1)
                            self.talk('Thank You')

                        except Exception:
                            print('Sorry !')
            except Exception:
                print('Error !')

    def tell_about(self, command, lines):
        result = wiki.search(command)
        for item in result:
            print(item)
            info = wiki.page(item)
            info_summary = wiki.summary(info, lines)
            print(info_summary)
            self.talk(info_summary)

    def talk(self, command):
        self.voice_engine.say(command)
        self.voice_engine.runAndWait()
        self.voice_engine.stop()

if __name__ == "__main__":
    tell_about_class = alexa_tell_me_about()
    tell_about_class.listen()
    system('pause')