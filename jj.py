import pygame
import pyttsx3
import time

# Initialize pygame for audio
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)  # Adjust the volume as needed

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()

# Define Morse code patterns for dot and dash
dot_duration = 0.2  # Adjust the duration in seconds
dash_duration = 0.6  # Adjust the duration in seconds

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

# Function to play Morse code audio
def play_morse_code(text):
    for char in text.upper():
        if char in morse_code_dict:
            code = morse_code_dict[char]
            for symbol in code:
                if symbol == '.':
                    pygame.mixer.music.load("dot.wav")  # Replace with your dot sound file
                    pygame.mixer.music.play()
                    time.sleep(dot_duration)
                elif symbol == '-':
                    pygame.mixer.music.load("dash.wav")  # Replace with your dash sound file
                    pygame.mixer.music.play()
                    time.sleep(dash_duration)
                else:
                    # Add a pause for space
                    time.sleep(dot_duration)
                print(symbol, end=' ')
        else:
            # Add a pause for space between words
            time.sleep(dash_duration)
            print("/", end=' ')

# Function to read out text using text-to-speech
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    message = "emergency mission abort"
    try:
        morse_message = ''.join([morse_code_dict.get(c, '') for c in message])
        print("Morse Code:", morse_message)
        play_morse_code(morse_message)
        speak_text(message)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
