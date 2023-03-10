import pyttsx3 # for text to speech conversion
import speech_recognition as sr # recognizing speech
import webbrowser # working with browsers
import datetime # datetime module
import pyjokes # some lame jokes


def sptext():
    recognizer = sr.Recognizer() # initiating recognizer
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
    engine = pyttsx3.init() # initializing pyttsx3
    voices = engine.getProperty('voices') # get voices
    engine.setProperty('voice', voices[0].id)  # use voices[1] for female voice
    rate = engine.getProperty('rate') # get the playback speed
    engine.setProperty('rate', 150) # increase or decrease playback speed by changing the value
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    if 'hey mango' in sptext().lower(): # activating assistant

        while True: # work infintely until you say exit
            data1 = sptext().lower() # lowers all the text you have spoken

            if "your name" in data1: # checking if "your name" is in your speech
                name = "my name is mango" # storing your answer
                speechtx(name) # speaking your answer

            elif "old are you" in data1:
                age = "I don't have a age as I am not physical being"
                speechtx(age)

            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p") # Hours:Minutes:PM/AM
                speechtx(time)

            elif "google" in data1:
                webbrowser.open('https://www.google.com')

            elif "joke" in data1:
                spjoke = pyjokes.get_joke(language="en", category="neutral")
                speechtx(spjoke)

            elif "exit" in data1: # to exit the code
                speechtx("Exiting. Thank you for using") # exiting message
                break # cut the loop

    else:
        speechtx("Thanks")
        print("Thank you")
