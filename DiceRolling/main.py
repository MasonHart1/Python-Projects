import random
import os
import subprocess

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    amount = int(input("How many would you like to roll?\n"))
    rolls = []

    while amount > 0:
        rolls.append(random.randint(1,6))
        amount -= 1

    for index, i in enumerate(rolls, 1):
        print(f"Dice {index}. {i}")
    input("Press enter to continue")

main()

choice = input("Would you like to roll again? (y/n)\n")

if choice == "y":
    main()
elif choice == "n":
    subprocess.run(['python', 'main.py'])