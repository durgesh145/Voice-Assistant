import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your voice assistant, Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vadaystar@gmail.com', 'vaday@12')
    server.sendmail('vadaystar@gmail.com','vadyvaday145@gmail.com', content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
             speak("opening youtube")
             webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'stack' in query:
            speak("opening stack overflow")
            webbrowser.open("https://stackoverflow.com/")

        elif 'gfg' in query:
            speak("opening geeks for geeks")
            webbrowser.open("https://www.geeksforgeeks.org/")

        elif 'amazon web service' in query:
            speak("opening aws website")
            webbrowser.open("https://aws.amazon.com/")

        elif 'online compiler' in query:
            speak("opening online compiler")
            webbrowser.open("https://ide.geeksforgeeks.org/")

        elif 'play' in query:
            video=query.replace('play','')
            speak('playing'+video)
            pywhatkit.playonyt(video)  

        elif 'send message' in query:
            speak("what should i send")
            text=takeCommand()
            pywhatkit.sendwhatmsg("+918090123604",text,7,33) 


        elif 'music' in query:
           music_dir = 'C:\\Users\\Durgesh Kumar\\Documents\\Assignment\\music'
           songs = os.listdir(music_dir)
           print(songs)    
           os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
           codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)

        elif 'cricket score' in query:
            webbrowser.open("cricbuzz.com")

        elif 'email to durgesh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vadayvaday145@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")   

        elif 'quit' in query:
            speak("Quitting sir.  Have a nice day")
            quit()