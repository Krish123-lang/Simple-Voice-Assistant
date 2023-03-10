import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:  # init Microphone
        print('Listening ...')
        recognizer.adjust_for_ambient_noise(source)  # noise cancellation
        audio = recognizer.listen(source)  # listen from the source

        try:
            print('recognizing...')
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print('Not Understand ...')


def speechtx(x):  # text to speech
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # use voices[1] for female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    if 'hey mango' in sptext().lower():

        while True:
            data1 = sptext().lower()

            if "your name" in data1:
                name = "my name is mango"
                speechtx(name)

            elif "old are you" in data1:
                age = "I don't have a age as I am not physical being"
                speechtx(age)

            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif "google" in data1:
                webbrowser.open('https://www.google.com')

            elif "joke" in data1:
                spjoke = pyjokes.get_joke(language="en", category="neutral")
                speechtx(spjoke)

            elif "exit" in data1:
                speechtx("Exiting. Thank you for using")
                break

    else:
        speechtx("Thanks")
        print("Thank you")
