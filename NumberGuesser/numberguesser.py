import random
import subprocess

num = random.randint(1, 100)


print('You have 5 tries, computer chose a random number from 1-100, try to guess it')
guess_count = 1

while guess_count < 6:
    user_choice = int(input(f'Guess #{guess_count}: '))
    if user_choice > num:
        print(f'Computers number is lower than {user_choice}')
    elif user_choice < num:
        print(f'Computer number is higher than {user_choice}')
    else:
        print(f'You guessed it! Computers number was {num}')
        choice = input("Play again? (yes or no): ")        
        if choice == "no":
            subprocess.run(['python', 'main.py'])
        else: 
            subprocess.run(['python', 'NumberGuessernumberguesser.py'])
    guess_count += 1
else:
    print(f"You failed... Computers number was {num}")
    choice = input("Play again? (yes or no): ")

    if choice == "no":
        subprocess.run(['python', 'main.py'])
    else: 
        subprocess.run(['python', 'NumberGuesser/numberguesser.py'])