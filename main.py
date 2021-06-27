import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pywhatkit
import pyjokes


def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 0.5
        audio = r.listen(source)

        # Now we will be using the try and catch method so that if sound is recognized
        # it is good ,else we will have exception handling
        try:
            print("Recognizing")

            query = r.recognize_google(audio, language='en-in')
            print("The command is :", query)

        except Exception as e:
            print(e)
            print("Please Say the command again")
            return "None"

        return query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)

    engine.say(audio)
    engine.runAndWait()


def tell_day():
    day = datetime.datetime.today().weekday() + 1

    day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def hello():
    speak("hello Dear I am your desktop assistant. Tell me how may I help you")


def take_query():
    hello()

    while True:
        # Converting the query to lower case so that most of the times query matches and we get correct output
        query = take_command().lower()

        if "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif "which day it is" in query:
            tell_day()

        elif "time" in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif 'are you single' in query:
            speak('I am in a relationship with wifi')

        elif 'i love you' in query:
            speak("I hate cheesy words. Don't say that again")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("I am Ruu. Your desktop Assistant")

        # This will exit and terminate the program
        elif "bye" in query:
            speak("Bye. See you soon. Take care.")
            exit()

        else:
            speak('Please say the command again.')


if __name__ == '__main__':

    take_query()
