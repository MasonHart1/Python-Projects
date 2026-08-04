import os
import json
import time
import keyboard
import subprocess


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

if os.path.exists("passwords.json"):
    with open("passwords.json", "r") as file:
        data = json.load(file)
else:
    data = {"entries": {}}


entries = data["entries"]


def print_entries():
    clear_console()
    for index, (username, password) in enumerate(entries.items(), start=1):
        print(f"{index}. Username: {username}; Password: {password}")
    print("\n\nPress esc when done")
    keyboard.wait("esc")
    navigation()


def add_entry():
    clear_console()
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    entries[username] = password
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)
    clear_console()
    print("Username and password successfully added")
    time.sleep(1)
    navigation()


def search_entries():
    clear_console()
    selection = input("Enter a username to search: ")
    if selection in entries:
        print(f"Password: {entries[selection]}")
    else:
        print(f'Username: "{selection}" not found')
    time.sleep(2)
    navigation()

def delete_entry():
    clear_console()
    selection = input("Enter username you would like to delete: ")
    if selection in entries:
        del entries[selection]
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Password successfully deleted")
    else:
        print(f'Username: "{selection}" not found')
    time.sleep(2)
    navigation()

def exit_app():
    clear_console()
    print("Exiting", end="", flush=True)

    for i in range(3):
        time.sleep(.75)
        print(".", end="", flush=True)
    print()
    time.sleep(.5)
    subprocess.run(['python', 'main.py'])

def navigation():
    clear_console()
    selection = input(
        "Navigation\n\n"
        "1. Add a password\n"
        "2. View passwords\n"
        "3. Search password\n"
        "4. Delete\n"
        "5. Exit\n"
    )
    match int(selection):
        case 1:
            add_entry()
        case 2:
            print_entries()
        case 3:
            search_entries()
        case 4:
            delete_entry()
        case 5:
            exit_app()


navigation()
