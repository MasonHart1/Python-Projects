#!/usr/bin/env python3.14.6

import subprocess
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import time

user_birthdate = input("Please enter your birthdate (mm-dd-yyy): ")

try:
    birthdate = dt.strptime(user_birthdate, "%m-%d-%Y")
except ValueError:
    print("Invalid date format. Please use the format mm-dd-yyyy")
    time.sleep(1.5)
    subprocess.run(['python', 'calculate.py'])

today = dt.now()

age = relativedelta(today, birthdate)

print(f'You are {age.years} years {age.months} months and {age.days} days old')


choice = input("Exit? (y/n): ").strip().lower()
if choice == "y": subprocess.run(['python', 'main.py'])
else: subprocess.run(['python', 'calculate.py'])