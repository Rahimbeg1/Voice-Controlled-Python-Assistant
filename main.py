from speech import (
    speak,
    listen
)

from commands import (
    process_command
)

from logger import logger

WAKE_WORDS = [
    "buddy",
    "assistant"
]


def main():

    logger.info(
        "Assistant Started"
    )

    speak(
        "Hello. How can I help you today?"
    )

    while True:

        word = listen()

        if not word:
            continue

        if (
            "exit" in word
            or
            "quit" in word
        ):

            logger.info(
                "Assistant Closed"
            )

            speak("Goodbye")

            break

        if any(
            wake_word in word
            for wake_word in WAKE_WORDS
        ):

            speak("Yes")

            command = listen()

            if not command:
                continue

            success = process_command(
                command
            )

            if not success:

                speak(
                    "Command not recognized"
                )


if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
        
        