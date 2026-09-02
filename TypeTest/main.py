import random
import tkinter as tk
import time

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language to learn.",
    "I am building my own typing speed test.",
    "Programming becomes easier with practice.",
    "The computer processes instructions very quickly."
]

chosen_sentence = random.choice(sentences)

root = tk.Tk()
root.geometry("600x400")
root.title("Type Speed Test")

title = tk.Label(
    root,
    text="Type the sentence below into the box",
    font=("Arial", 20),
)
title.pack()

sentence_label = tk.Label(
    root,
    text=chosen_sentence,
    font=("Arial", 16),
    wraplength=500
)

sentence_label.pack(pady=30)

typing_box = tk.Entry(root, font=("Arial", 16), width=500)
typing_box.pack(pady=10, padx=25)

start_time = None
started = False

def start_test():
    global start_time, started
    started = True

    start_time = time.time()

    print("Started")

typing_box.focus()

def handle_keypress(event):
    global started
    if started:
        if event.keycode == 13:
            end_test()
            started = False
            print("Finished")
    else:
        if event.keysym != "Shift_L":
            start_test()
root.bind("<Key>", handle_keypress)

def end_test():
    global start_time

    correct = 0

    elapsed_time = int(time.time()) - int(start_time)
    typed_text = typing_box.get()
    words = len(typed_text) / 5
    wpm = words / (elapsed_time / 60)
    for i in range(min(len(chosen_sentence), len(typed_text))):
        if chosen_sentence[i] == typed_text[i]:
            correct += 1
    accuracy = (correct / len(chosen_sentence)) * 100

    message = f"You typed {int(wpm)} words per minute at {round(accuracy, 2)}% accuracy"
    tk.Label(root, text=message, font=("Arial", 18), wraplength=500).pack()

root.mainloop()