import speech_recognition as engine
import pyaudio, datetime
import pywhatkit as kit
import pyttsx3 as text_to_speech
import wikipedia as wiki
import pyjokes as joker
import os

# Author : Imtiaz Adar
# Project : Automate Alexa
# Language : Python

listener = engine.Recognizer()
# getting Alexa's voice
speech_engine = text_to_speech.init()
voices = speech_engine.getProperty('voices')
speech_engine.setProperty('voice', voices[1].id)
command = ''

def listen_command():
    global command
    with engine.Microphone() as mic:
        print('Listening...')
        listener.adjust_for_ambient_noise(mic)
        voice_of_mine = listener.listen(mic)
    try:
        command = listener.recognize_google(voice_of_mine)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(f'Your command : {command}')
            if 'play' in command:
                play_song(command)
                play_command = command.replace('play', '')
                talk(f'Playing {play_command}')
                print(f'Playing {play_command}')
                print('Played')

            elif 'time' in command:
                talk(f'Telling the time')
                time = tell_time()
                time_now = f'Current time is {time}'
                print(time_now)
                talk(time_now)

            elif 'date' in command:
                talk(f'Telling the date')
                date = tell_date()
                date_now = f"Today is {date}"
                print(date_now)
                talk(date_now)

            elif 'tell me about' in command:
                person = command.replace('tell me about', '')
                information_of_the_person = informations_from_wiki(person)
                print(information_of_the_person)
                talk(information_of_the_person)

            elif 'tell me a joke' in command:
                new_command = command.replace('tell me a joke', '')
                joke = tell_joke(new_command)
                print(joke)
                talk(joke)

    except Exception:
        print('Error !')

def play_song(command):
    song_name = command.replace('play', '')
    kit.playonyt(song_name)

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return current_time

def tell_date():
    todays_date = datetime.datetime.now().strftime("%d %B %Y - %A")
    return todays_date

def informations_from_wiki(command):
    return wiki.summary(command, 1)

def tell_joke(command):
    return joker.get_joke()

def talk(command):
    speech_engine.say(command)
    speech_engine.runAndWait()
    speech_engine.stop()

if __name__ == "__main__":
    print('AUTOMATE ALEXA - Imtiaz Adar')
    print('[[ COMMANDS ]]\nAlexa, Play [Music Name]\nAlexa, [Say Something] Time\n'
          'Alexa, [Say Something] Date\n'
          'Alexa, Tell Me About [Person]'
          '\nAlexa, Tell Me A Joke\n')
    listen_command()
    stat = True
    while stat:
        anymore_command = input('Anymore Command ?\nY/ Yes\nN/ No')
        if anymore_command.lower() == 'y':
            listen_command()
        else:
            stat = False
    os.system('pause')