import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser as web
from AppOpener import run
import subprocess
import os
import time
import pyjokes

listener = sr.Recognizer()
machine = pyttsx3.init()
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[0].id)


def talk(text):
    machine.say(text)
    machine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
            elif 'hey jarvis' in command:
                command = command.replace('hey jarvis', '')
                print(command)

    except sr.UnknownValueError:
        talk('sorry, i did not get that')
    except sr.RequestError:
        talk('sorry, the service is down')
        return 'None'
    return command


def run_jarvis():
    running = True
    a1 = 'hii sir'
    a2 = 'what can i do for you'
    print(a1)
    talk(a1)
    print(a2)
    talk(a2)
    while running:
        command = take_command()
        if 'play' in command:
            song = command.replace('play', '')
            talk("playing" + song)
            pywhatkit.playonyt(song)
            time.sleep(5)
        elif 'open youtube' in command and 'play' not in command:
            talk('opening youtube')
            web.open('www.youtube.com')
        elif 'flipkart' in command:
            talk('opening flipkart')
            web.open('www.flipkart.com')
            time.sleep(3)
        elif 'search' in command:
            k2 = command.replace('search', '')
            k3 = command.replace('search', 'searching')
            talk(k3)
            pywhatkit.search(k2)
        elif 'google' in command:
            k4 = command.replace('google', '')
            k5 = command.replace('google', 'searching')
            talk(k5)
            pywhatkit.search(k4)
        elif 'meaning' in command:
            k6 = command
            pywhatkit.search(k6)
        elif 'how' in command:
            p1 = command
            p11 = wikipedia.search(p1, 2)
            print(p11)
            talk(p11)
        elif 'what can you do' in command:
            p2 = 'playing songs on youtube'
            p3 = 'opening apps'
            talk(' I can do some basic tasks like sending whatsapp message' + p2 + p3)
        elif 'what will you do' in command:
            p4 = 'playing songs on youtube'
            p5 = 'opening apps'
            talk(' I can do some basic tasks like sending whatsapp message' + p4 + p5)
        elif 'what' in command:
            p6 = command
            p61 = wikipedia.summary(p6, 2)
            print(p61)
            talk(p61)
        elif 'where' in command:
            p7 = command
            p71 = wikipedia.search(p7, 2)
            print(p71)
            talk(p71)

        elif 'why' in command:
            p8 = command
            p81 = wikipedia.search(p8, 2)
            print(p81)
            talk(p81)
            time.sleep(10)
        elif 'when' in command:
            p9 = command
            p10 = wikipedia.search(p9, 2)
            print(p10)
            talk(p10)
            time.sleep(2)
        elif 'open chrome' in command:
            k7 = command.replace('open chrome', 'opening chrome')
            talk(k7)
            web.open('www.chrome.com')
        elif 'time' in command:
            tym = datetime.datetime.now().strftime('%I:%M %p')
            print(tym)
            talk('current time is' + tym)
        elif 'today' and 'date' in command:
            date = datetime.datetime.today().strftime('%d-%m-%y')
            print(date)
            talk(date)
        elif 'notepad' in command:
            talk('opening notepad')
            os.system('notepad.exe')
        elif 'cmd' in command:
            talk('opening command prompt')
            os.system('cmd.exe')
        elif 'command prompt' in command:
            talk('opening command prompt')
            os.system('cmd.exe')
        elif 'calculator' in command:
            talk(' opening calculator')
            os.system('calc.exe')
        elif 'ppt' in command:
            talk('opening microsoft powerpoint')
            run('powerpoint')
        elif 'excel' in command:
            talk('opening ms excel')
            run('excel')
        elif 'open mail' in command:
            talk('opening mail')
            run('mail')
        elif 'vlc' in command:
            talk('opening vlc player')
            subprocess.call("C:/Program Files (x86)/VideoLAN/VLC/vlc.exe")
        elif 'screenshot' in command:
            talk('taking screenshot')
            pywhatkit.take_screenshot('screenshot')
        elif 'who is' in command:
            person = command
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'suggest' in command:
            h1 = command
            h2 = wikipedia.search(h1, 2)
            print(h2)
            talk(h2)
        elif 'whatsapp' in command:
            talk('please tell me the number')
            num = take_command()
            talk(num)
            num = str(num)
            num2 = '+91' + num
            talk('what is the message')
            msg = take_command()
            talk(msg)
            msg2 = str(msg)
            talk('sending message')
            pywhatkit.sendwhatmsg_instantly(num2, msg2, 15, True, 3)
            talk('message sent')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            joke2 = pyjokes.get_joke()
            print(joke)
            talk(joke)
            talk('would you like to hear another one sir')
            s2 = take_command()
            if 'yes' or 'yeah' or 'another joke' in s2:
                print(joke2)
                talk(joke2)
        elif 'you love me' in command:
            t1 = 'i love you'
            print(t1)
            talk(t1)
        elif 'love you' in command:
            t3 = 'you are very sweet,i love you too'
            print(t3)
            talk(t3)
        elif 'who are you' in command:
            talk("iam jarvis, iam your voice assistant")
        elif 'your name' in command:
            talk("iam jarvis, sir")
        elif 'hello' in command:
            talk('hello sir, how can i help you')
        elif 'go to sleep' in command:
            t2 = 'ok sir'
            talk(t2)
            running = False
        elif 'bye' in command:
            talk('bye sir')
            running = False
        elif 'turn off' in command:
            talk('turning off')
            running = False
        else:
            talk('sorry! please say again')


if __name__ == '__main__':
    run_jarvis()
