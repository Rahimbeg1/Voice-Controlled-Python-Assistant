
import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait() 



if __name__ == "__main__":
    speak("Hello, How can I help you today?")
    while True:
        r=sr.Recognizer()
        print("Please give a command:")
        try:
            
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source )
            word = r.recognize_google(audio)
            print(f"You said: {word}")
            
            if "Betu" in word:
                speak("Yes")
                
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"You said: {command}")
                if "open Google" in command:
                     webbrowser.open("https://www.google.com")
                     speak("Opening Google")    
                elif "open YouTube" in command:
                     webbrowser.open("https://www.youtube.com")
                     speak("Opening YouTube") 
                elif "open Facebook" in command:
                     webbrowser.open("https://www.facebook.com")
                     speak("Opening Facebook")        
                elif "open music" in command:
                    from music_lib import music
                    speak("Opening music")
                    for song, url in music.items():
                        print(f"Opening {song}")
                        webbrowser.open(url)
                elif "open Instagram" in command:
                     webbrowser.open("https://www.instagram.com")
                     speak("Opening Instagram")
                elif "open Twitter" in command:
                     webbrowser.open("https://www.twitter.com")
                     speak("Opening Twitter")
                elif "open LinkedIn" in command:
                     webbrowser.open("https://www.linkedin.com")
                     speak("Opening LinkedIn")
                elif "open WhatsApp" in command:
                     webbrowser.open("https://web.whatsapp.com")
                     speak("Opening WhatsApp")
            
            elif "exit" in word or "quit" in word:
                speak("Goodbye!")
                break
           
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       