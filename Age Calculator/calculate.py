import subprocess
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import time

user_name = input("Please enter your name: ")

user_birthdate = input("Please enter your birthdate (mm-dd-yyy): ")

try:
    birthdate = dt.strptime(user_birthdate, "%m-%d-%Y")
except ValueError:
    print("Invalid date. please use the format mm-dd-yyyy")
    time.sleep(1.5)
    subprocess.run(['python', 'Python Projects/Age Calculator/calculate.py'])

today = dt.now()

age = relativedelta(today, birthdate)

print(f'{user_name} is {age.years} years {age.months} months and {age.days} days old')


choice = input("Exit? (yes or no): ").strip().lower()
if choice == "yes": subprocess.run(['python', 'Python Projects/main.py'])
else: subprocess.run(['python', 'Python Projects/Age Calculator/calculate.py'])