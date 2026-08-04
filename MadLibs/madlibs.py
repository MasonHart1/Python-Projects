# array of paragraphs
# array of arrays for nouns verbs adjectives
# choose paragraph
# 2 random nouns verbs and adjectives from corresponding paragraph
# get user inputs
import re
import tkinter as tk
import subprocess

paragraphs = [
    """
    Today I woke up feeling {adjective}, so I grabbed my {noun} and rand to the {place}. Suddenly, a {adjective2} {animal} appeared and started {verb_ending_in_ing} around me
    """,
    """
    When I got to school, my {noun} was missing! My teacher, {name} told me to {verb} as fast as possible. Instead I accidentally {past_tense_verb} into the {room} and knocked over {number} {plural_noun}. Everyone started {verb_ending_in_ing} while I turned {color} with embarrassment.
    """,
    """
    Captain {name} climbed aboard the {adjective} spaceship and blasted off toward {planet}. Along the way, they discovered a {adjective1} alien carrying a {noun}. The alien asked if humans enjoy {verb_ending_in_ing} with {plural_noun}. After {number} hours, the crew safely returned to Earth with the most {adjective2} story ever told.
    """,
    """
    Welcome to {adjective} cooking! Today we're making {food} using only a {noun}, {number}, {plural_noun}, and a pinch of {silly_word}. First, {verb} everything together until it becomes {adjective1}. Then bake it for {number} minutes before serving it to your favorite {animal}. If they {verb1} happily, congratulations - you've created the world's {adjective2} recipe!
    """,
]

words = {}

root = tk.Tk()
root.title("Main Window")
root.geometry("500x500")

choose_label = tk.Label(
    root, text="Please choose a paragraph 1-4", font=("Calibri", 11)
)
choose_entry = tk.Entry(root, font=("Calibri", 11))
choose_label.grid(row=0, column=0, pady=5, padx=5)
choose_entry.grid(row=0, column=1, pady=5, padx=5)

entries = {}

def choose_paragraph():
    global story

    story = paragraphs[int(choose_entry.get()) - 1]
    placeholders = re.findall(r"{(.*?)}", story)

    entries.clear()

    for row, placeholder in enumerate(placeholders, start=2):
        tk.Label(
            root, text=placeholder.replace("_", " ").title() + ":", font=("Calibri", 11)
        ).grid(row=row, column=0, sticky="w", padx=5, pady=5)

        entry = tk.Entry(root, width=30)
        entry.grid(row=row, column=1, padx=5, pady=5)

        entries[placeholder] = entry

    submit_button = tk.Button(
        root, text="Submit", font=("Calibri", 13), command=submit
    )
    submit_button.grid(column=1)


choose_button = tk.Button(
    root, text="Select", font=("Calibri", 13), command=choose_paragraph
)
choose_button.grid(row=1, column=1)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def submit():
    for placeholder, entry in entries.items():
        words[placeholder] = entry.get()

    print(words)
    clear_window()
    print(story.format(**words))
    story_label = tk.Label(
        root, text=story.format(**words), font=("Calibri", 25), pady=5,padx=5
    )
    story_label.grid(row=0,column=0)
    root.update_idletasks()
    auto_width = root.winfo_reqwidth()
    custom_height = 500
    root.geometry(f"{auto_width}x{custom_height}")


def onclosing():
    root.destroy()
    subprocess.run(['python', 'main.py'])

root.protocol("WM_DELETE_WINDOW", onclosing)

root.mainloop()