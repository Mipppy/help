from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

#Speech engine

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id) #0: male 1: female
activationWord = 'pass'
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)


    try:
        print('recognizing speech')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')

    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'
    return query

if __name__ == '__main__':
    speak('All systems normal')

    while True:
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greeting')
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)
            if query[0] == 'go' and query[1] == 'to':
                speak("Opening...")
                query = ' '.join(query[2:])
                webbrowser.get('chrome').open_new(query)




