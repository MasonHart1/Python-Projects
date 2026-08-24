from pathlib import Path
import subprocess
import os
import time
import sys

try:
    from config_local import PYTHON_312, PYTHON_314
    print("Loaded")
    time.sleep(5)
except ImportError:
    print("Not Loaded")
    time.sleep(5)
    PYTHON_312 = "python3.12"
    PYTHON_314 = "python3.14"
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    print("--NAVIGATION--")
    menu = """
    1. Age Calculator
    2. Calculator
    3. Hangman
    4. MadLibs
    5. Number Guesser
    6. Password Manager
    7. Random Password Generator
    8. Rock Paper Scissors
    9. Tic Tac Toe
    10. To-do List
    11. MP3 Player
    12. Morse Code Translator
    13. Unit Converter
    14. Quiz Game
    15. Exit
"""
    print(menu)
    try:
        num = int(input("Enter the number of the project you want to open: "))
    except ValueError:
        clear()
        print("Invalid input, try again")
        time.sleep(1.5)
        main()
        return

    clear()
    if not 1 <= num <= len(menu.strip().split("\n")): 
        print("Invalid input, try again")
        time.sleep(1.5)
        main()
        return
    match num:
        case 1: subprocess.run([PYTHON_314, 'Age Calculator/calculate.py'])
        case 2: subprocess.run([PYTHON_314, 'Calculator/calculator.py'])
        case 3: subprocess.run([PYTHON_314, 'Hangman/hangman.py'])
        case 4: subprocess.run([PYTHON_314, 'MadLibs/madlibs.py'])
        case 5: subprocess.run([PYTHON_314, 'NumberGuesser/numberguesser.py'])
        case 6: subprocess.run([PYTHON_314, 'PasswordManager/passwordmanager.py'])
        case 7: subprocess.run([PYTHON_314, 'Random Password Generator/main.py'])
        case 8: subprocess.run([PYTHON_314, 'RPS/rps.py'])
        case 9: subprocess.run([PYTHON_314, 'TicTacToe/tictactoe.py'])
        case 10: subprocess.run([PYTHON_314, 'TodoList/todolist.py'])
        case 11: subprocess.run([PYTHON_312, 'Musicplayer/main.py'])
        case 12: subprocess.run([PYTHON_314, 'MorseCodeTranslator/main.py'])
        case 13: subprocess.run([PYTHON_314, 'UnitConverter/main.py'])
        case 14: subprocess.run([PYTHON_314, 'QuizGame/main.py'])
        case 15: print("Goodbye!"); time.sleep(1.5); clear()

main()