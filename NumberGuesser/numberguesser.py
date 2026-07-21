import random

num = random.randint(1, 100)


print('Computer chose a random number from 1-100, try to guess it')
guess_count = 1

while True:
    user_choice = int(input(f'Guess #{guess_count}: '))
    if user_choice > num:
        print(f'Computers number is lower than {user_choice}')
    elif user_choice < num:
        print(f'Computer number is higher than {user_choice}')
    else:
        print(f'You guessed it! Computers number was {num}')
        break
    guess_count += 1