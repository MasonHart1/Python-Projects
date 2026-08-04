from pathlib import Path
import subprocess
import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    print("--NAVIGATION--")
    print("""
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
    11. Exit
""")
    try:
        num = int(input("Select where you want to go: "))
    except ValueError:
        clear()
        print("Invalid input, try again")
        time.sleep(1.5)
        main()
        return

    clear()
    if not 1 <= num <= 11: 
        print("Invalid input, try again")
        time.sleep(1.5)
        main()
        return
    match num:
        case 1: subprocess.run(['python', 'Python Projects/Age Calculator/calculate.py'])
        case 2: subprocess.run(['python', 'Python Projects/Calculator/calculator.py'])
        case 3: subprocess.run(['python', 'Python Projects/Hangman/hangman.py'])
        case 4: subprocess.run(['python', 'Python Projects/MadLibs/madlibs.py'])
        case 5: subprocess.run(['python', 'Python Projects/NumberGuesser/numberguesser.py'])
        case 6: subprocess.run(['python', 'Python Projects/PasswordManager/passwordmanager.py'])
        case 7: subprocess.run(['python', 'Python Projects/Random Password Generator/main.py'])
        case 8: subprocess.run(['python', 'Python Projects/RPS/rps.py'])
        case 9: subprocess.run(['python', 'Python Projects/TicTacToe/tictactoe.py'])
        case 10: subprocess.run(['python', 'Python Projects/TodoList/todolist.py'])
        case 11: os.abort()

main()