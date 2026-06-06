import webbrowser

from speech import speak
from logger import logger

from system_monitor import (
    cpu_usage,
    ram_usage,
    battery_status,
    disk_usage,
    network_status,
    uptime
)

from music_lib import music


def open_google():

    logger.info("Opening Google")

    webbrowser.open(
        "https://www.google.com"
    )

    speak("Opening Google")


def open_youtube():

    logger.info("Opening YouTube")

    webbrowser.open(
        "https://www.youtube.com"
    )

    speak("Opening YouTube")


def open_instagram():

    logger.info("Opening Instagram")

    webbrowser.open(
        "https://www.instagram.com"
    )

    speak("Opening Instagram")


def open_linkedin():

    logger.info("Opening LinkedIn")

    webbrowser.open(
        "https://www.linkedin.com"
    )

    speak("Opening LinkedIn")


def open_whatsapp():

    logger.info("Opening WhatsApp")

    webbrowser.open(
        "https://web.whatsapp.com"
    )

    speak("Opening WhatsApp")


def play_music():

    logger.info("Playing Music")

    speak("Opening Music")

    for song, url in music.items():

        print(f"Opening {song}")

        webbrowser.open(url)


def cpu_status():
    speak(cpu_usage())


def ram_status():
    speak(ram_usage())


def battery_info():
    speak(battery_status())


def disk_info():
    speak(disk_usage())


def network_info():
    speak(network_status())


def uptime_info():
    speak(uptime())