import random
import os
import time
import subprocess

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

choices = ["rock", "paper", "scissors"]
game_num = 0
plr_wins = 0
ai_wins = 0

def ai_random():
    choice = random.choice(choices)
    return choice

def start_game():
    global plr_wins, ai_wins

    while plr_wins < 3 and ai_wins < 3:
        clear_console()
        print(f"\nScore: User {plr_wins} - {ai_wins} AI\n")
        ai_choice = ai_random()
        user_choice = input(
            "AI has made its selection. Choose rock, paper, or scissors:\n"
        ).lower()

        if user_choice == "rock":
            if ai_choice == "paper":
                print(f"User: {user_choice} vs. AI: {ai_choice}\nAI GETS A POINT!")
                ai_wins += 1
            elif ai_choice == "scissors":
                print(f"User: {user_choice} vs. AI: {ai_choice}\nUSER GETS A POINT!")
                plr_wins += 1
            else:
                print(f"User: {user_choice} vs. AI: {ai_choice}\nIT'S A TIE!")

        elif user_choice == "paper":
            if ai_choice == "rock":
                print(f"User: {user_choice} vs. AI: {ai_choice}\nUSER GETS A POINT!")
                plr_wins += 1
            elif ai_choice == "scissors":
                print(f"User: {user_choice} vs. AI: {ai_choice}\nAI GETS A POINT!")
                ai_wins += 1
            else:
                print(f"User: {user_choice} vs. AI: {ai_choice}\nIT'S A TIE!")

        elif user_choice == "scissors":
            if ai_choice == "rock":
                print(f"User: {user_choice} vs. AI: {ai_choice}\nAI GETS A POINT!")
                ai_wins += 1
            elif ai_choice == "paper":
                print(f"User: {user_choice} vs. AI: {ai_choice}\nUSER GETS A POINT!")
                plr_wins += 1
            else:
                print(f"User: {user_choice} vs. AI: {ai_choice}\nIT'S A TIE!")
        else:
            print("Invalid choice!")
        time.sleep(2)


    if plr_wins == 3:
        clear_console()
        print("GAME OVER USER WINS")
        choice = input("Play again? (yes or no): ").strip().lower()
        if choice == "no":
            subprocess.run(['python', 'Python Projects/main.py'])
        else: subprocess.run(['python', 'Python Projects/RPS/rps.py'])
    else:
        clear_console()
        print("GAME OVER AI WINS")
        choice = input("Play again? (yes or no): ").strip().lower()
        if choice == "no":
            subprocess.run(['python', 'Python Projects/main.py'])
        else: subprocess.run(['python', 'Python Projects/RPS/rps.py'])

start_game()