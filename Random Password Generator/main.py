import random
import subprocess

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=/?'

password = ''

for x in range(16):
    password += random.choice(chars)

print(password)
choice = input ('New password? (y/n): ').strip().lower()

if choice == "n":
    subprocess.run(['python', 'main.py'])
else: subprocess.run(['python', 'Random Password Generator/main.py'])