import random
import os
import time
from pyfiglet import Figlet
import subprocess

f = Figlet(font='doom')


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

words = [
    "python", "computer", "keyboard", "monitor", "program",
    "hangman", "science", "variable", "function", "library",
    "elephant", "mountain", "penguin", "diamond", "galaxy",
    "chocolate", "adventure", "airplane", "baseball", "treasure"
]

word = random.choice(words)
print(word)

phase = 0

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

user_guesses = ''

clear_console()

while True:
    clear_console()
    print(HANGMANPICS[phase])
    print(user_guesses)

    for letter in word:
        if letter in user_guesses:
            print(letter, end =' ')
        else:
            print("_", end=' ')
    print()
    if phase > 5:
        print(f'The word was {word}')
        print(f.renderText('You lose'))
        choice = input("Play again? (yes or no): ").strip().lower()                
        if choice == "no":
            subprocess.run(['python', 'Python Projects/main.py'])
        else: subprocess.run(['python', 'Python Projects/Hangman/hangman.py'])

    if all(letter in user_guesses for letter in word):
        print(f.renderText("You win!"))
        choice = input("Play again? (yes or no): ").strip().lower()
        
        if choice == "no":
            subprocess.run(['python', 'Python Projects/main.py'])
        else: subprocess.run(['python', 'Python Projects/Hangman/hangman.py'])
            
    letter_guess = input('Guess a letter: ')



    if len(letter_guess) != 1 or not letter_guess.isalpha() or user_guesses.__contains__(letter_guess):
        print('Not Valid guess')
        time.sleep(.5)
        continue
    user_guesses += letter_guess
    if letter_guess not in word:
        phase += 1