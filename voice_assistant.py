import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
#engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
volume=.5
engine.setProperty("volume",volume)
#engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command=""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        return True
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
        return True
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        return True
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        return True
    elif 'thank you' in command:
        talk('you are welcome')
        return False
    else:
        talk('Please say the command again.')
        return True

a=True
while a==True:
    a=run_alexa()
print('Closing...')
