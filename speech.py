import speech_recognition as sr
import pyttsx3
from logger import logger

engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        logger.info(f"User said: {command}")

        print(f"You said: {command}")

        return command.lower()

    except sr.UnknownValueError:

        logger.warning(
            "Speech could not be recognized"
        )

        speak("I did not understand that.")

        return ""

    except Exception as e:

        logger.error(
            f"Speech Error: {e}"
        )

        return ""