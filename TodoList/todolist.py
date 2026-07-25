def add_to_list():
    adding = input("Please enter task name")
    list_entries.append({"name": adding, "completed": False})
    print(f"Successfully added {adding} to your list")
    navigation()
def view_list():
    for index, task in enumerate(list_entries, start=1):
        status = "✅" if task['completed'] else "❌"
        print(f"{index}) {task['name']} ({status})")
        
        navigation()
#def mark_complete():
#def delete_from_list():
#def exit_app()

list_entries = []

def navigation():
    print("\n-----NAVIGATION-----")
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
        case 5: exit_app()

navigation()