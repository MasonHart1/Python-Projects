import json
import time
import os
from pynput import keyboard
import subprocess

def backtomain():
    subprocess.run(['python', 'Python Projects/main.py'])

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        data = json.load(file)
else: data = {"tasks": []}

tasks = data["tasks"]

def add_to_list():
    clear_console()
    adding = input("Please enter task name: ")
    tasks.append({"name": adding, "completed": False})
    save_tasks()
    print(f"Successfully added {adding} to your list")
    time.sleep(2)
    navigation()

def on_press(key):
    if key == keyboard.Key.esc:
        return False

def view_list():
    clear_console()
    tasks.sort(key=lambda task: not task['completed'])
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task['completed'] else "❌"
        print(f"{index}) {task['name']} {status}")

    print("\nPress esc when done viewing")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    navigation()

def mark_complete():
    clear_console()
    tasks.sort(key=lambda task: not task['completed'])
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task['completed'] else "❌"
        print(f"{index}) {task["name"]} {status}")
    task = int(input("\n\nSelect a task to mark complete: "))
    tasks[task - 1]["completed"] = True
    clear_console()
    print(f"Task {tasks[task - 1]["name"]} successfully marked as complete")
    save_tasks()
    time.sleep(2)
    navigation()
def delete_from_list():
    clear_console()
    tasks.sort(key=lambda task: not task['completed'])
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task['completed'] else "❌"
        print(f"{index}) {task["name"]} {status}")
    task = int(input("\n\nPlease select a task to delete: ")) - 1
    clear_console()
    print(f"Successfully deleted task: {tasks[task]["name"]}")
    tasks.pop(task)
    save_tasks()
    time.sleep(2)
    navigation()

list_entries = []

def navigation():
    clear_console()
    print("-----NAVIGATION-----")
    print(
    """
    1) Add to list
    2) View List
    3) Mark as complete
    4) Delete from list
    5) Exit
    """)
    choise = input("Select an option (1-5): ")
    match int(choise):
        case 1: add_to_list()
        case 2: view_list()
        case 3: mark_complete()
        case 4: delete_from_list()
        case 5: subprocess.run(['python', 'main.py'])

navigation()
