import subprocess
from pynput import keyboard


def on_press(key):
    if key == keyboard.Key.esc:
        subprocess.run(["python", "main.py"])

morse_to_letter = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}

letter_to_morse = {v: k for k, v in morse_to_letter.items()}

if input("Do you want to convert Morse code to letters? (y/n): ").lower() == 'y':
    morse_code = input("Enter Morse code (use spaces between letters and '/' for spaces between words): ")
    words = morse_code.split(' / ')
    translated_words = []
    for word in words:
        letters = word.split(' ')
        translated_word = ''.join(morse_to_letter.get(letter, '') for letter in letters)
        translated_words.append(translated_word)
    translated_text = ' '.join(translated_words)
    print("Translated text:", translated_text)
elif input("Do you want to convert letters to Morse code? (y/n): ").lower() == 'y':
    text = input("Enter text (letters only, use spaces between words): ")
    words = text.upper().split(' ')
    translated_words = []
    for word in words:
        morse_letters = [letter_to_morse.get(letter, '') for letter in word]
        translated_word = ' '.join(morse_letters)
        translated_words.append(translated_word)
    translated_morse = ' / '.join(translated_words)
    print("Translated Morse code:", translated_morse)

print("Press Escape key to exit..")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
