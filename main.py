import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import random
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    """Converts text to speech and speaks it aloud."""
    engine.say(text)
    engine.runAndWait()


def take_command():
    """Listens for a command and converts speech to text."""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)  # Helps with background noise
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"Recognized Command: {command}")
                return command
            "Implementation of K nearest neighbour; "
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError:
        print("Could not request results, check internet connection")
    except Exception as e:
        print(f"Error: {e}")

    return ""  # Return empty string if no valid command is received


def play_music():
    """Plays a random song from the music folder."""
    music_dir = "C:\\Users\\adars\\Music"  # Change this to your actual music directory
    try:
        songs = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
        if songs:
            song = random.choice(songs)
            song_path = os.path.join(music_dir, song)
            os.startfile(song_path)  # Opens the file with the default player
            talk(f"Playing {song}")
        else:
            talk("No music files found in your music directory.")
    except Exception as e:
        print(f"Error playing music: {e}")
        talk("I couldn't play the music due to an error.")


def run_alexa():
    """Processes voice commands and executes appropriate functions."""
    command = take_command()

    if not command:
        return  # Skip processing if no valid command

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif 'music' in command or 'song' in command:
        play_music()

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"Current time is {time}")

    elif 'who is' in command or 'what is' in command:
        try:
            person = command.replace('who is', '').replace('what is', '').strip()
            info = wikipedia.summary(person, sentences=1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            talk("There are multiple results for that, please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find any information on that.")

    elif 'date' in command:
        talk("Sorry, I have a headache.")

    elif 'are you single' in command:
        talk("I am in a relationship with WiFi.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'exit' in command or 'stop' in command or 'bye' in command:
        talk("Goodbye! Have a great day.")
        exit()

    else:
        talk("I didn't understand that. Please say the command again.")


while True:
    run_alexa()