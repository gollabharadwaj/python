import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import msvcrt as m
import os
import subprocess

def wait():
    m.getch()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    talk('I am Miskeen ali personal assistant rolex ')
    wish = (datetime.datetime.now().strftime("%p"))
    if wish=='AM':
        
        talk('good morning')
    else:
        talk('good evening ')
wishMe()



def take_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return command
def run_rolex():
    command = take_command().lower()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif  command=='hai':
        talk('hello!')
    elif command=='how are you':
        talk('i am fine. what about you')
    elif command=='who are your parents':
        talk('i was created by my team KG10')
    elif command=='are you single':
        talk('no!! i am commited')
    elif command=='what is your number':
        talk('my ip is 192.15.36.285')
    elif command=='rolex':
        talk('hi how can i help you')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        wait()
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
        wait()
    elif 'date' in command:
        date=datetime.datetime.now().strftime('%x')
        talk('current date is'+date)
        wait()
    elif ' youtube' in command:
        webbrowser.open("https://www.youtube.com/")
        wait()

    elif 'open google' in command:
        subprocess.call(r"C:\Program Files\Google\Chrome\Application/chrome.exe")
        wait()
    elif 'open spotify' in command:
        webbrowser.open("https://open.spotify.com/") 
        wait()
    

  
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        wait()

    elif 'my music' in command:
        talk('playing')
        webbrowser.open("https://www.youtube.com/watch?v=hCt-H4-5wco&list=RDhCt-H4-5wco&start_radio=1")    
        wait()

    elif 'whatsapp' in command:
        talk('opening whatsaapp')
        webbrowser.open("https://web.whatsapp.com/")
        wait()
    elif 'mail' in command:
        talk('opening mail')
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        wait()
    elif 'maps' in command:
        talk('opening maps')
        webbrowser.open("https://www.google.com/maps")
        wait()
    elif 'neocolab' in command:
        talk('opening mail')
        webbrowser.open("https://neocolab.srmap.edu.in/")
        wait()
    elif 'movies'==command:
        talk('opening mail')
        webbrowser.open("https://ww4.ibomma.cc/telugu-movies/")
        wait()    
    elif 'linkedin' in command:
        talk('opening linkedin')
        webbrowser.open("https://in.linkedin.com/")
        wait()
    elif 'netflix' in command:
        talk('opening netflix')
        webbrowser.open("https://www.netflix.com/in/")
        wait()
    elif 'prime' in command:
        talk('opening prime')
        webbrowser.open("https://www.primevideo.com/in")
        wait() 
    elif 'gopal' == command:
        talk('opening GK in Browser')
        webbrowser.open("https://gopalakrishnaparimi.blogspot.com/")
        wait()

    elif "wait"==command:
        wait()
    else:
        talk('Please say the command again.')

    while True:
        run_rolex()


