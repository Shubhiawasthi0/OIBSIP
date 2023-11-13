import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak a response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand your command.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

# Main loop
while True:
    command = listen()

    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "how are you?" in command:
        speak("I am fine! what about you?")
    elif "play" in command:
        song = command.replace('play', "")
        speak("Playing.." +song)
        pywhatkit.playonyt(song)
        break
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M%p')
        speak('Current Time' +time)
    elif "date" in command:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        speak('Todays Date' +date)

    elif "goodbye" in command:
        speak("Yeah,Goodbye!")
        break
    else:
        speak("I'm sorry, I do not understand that command.")
        break