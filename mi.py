import time
from playsound import playsound
import pyttsx3

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' '
}

def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(c, '') for c in text.upper())

def play_morse_symbol(symbol):
    if symbol == '.':
        playsound('C:/Users/sravy/Desktop/14/dot.wav')
    elif symbol == '-':
        playsound('C:/Users/sravy/Desktop/14/dash.wav')
    elif symbol == ' ':
        playsound('C:/Users/sravy/Desktop/14/blank.wav')
        time.sleep(0.3)
    time.sleep(0.1)

def play_morse_code(morse_code):
    for symbol in morse_code:
        play_morse_symbol(symbol)

def speak_message(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
###done and its perfect
def main():
    message = input("enter the message = ")
    try:
        morse_message = text_to_morse(message)
        print("Morse Code:", morse_message)
        play_morse_code(morse_message)
        speak_message(message)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
