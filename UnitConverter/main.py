import tkinter as tk
from tkinter import ttk
import subprocess

conversion_logic = {
    "Meters": 1,
    "Kilometers": 1000,
    "Centimeters": 0.01,
    "Millimeters": 0.001,
    "Miles": 1609.34,
    "Yards": 0.9144,
    "Feet": 0.3048,
    "Inches": 0.0254
}

def calculate_conversion():
    amount = float(amount_input.get())
    from_unit = from_value.get()
    to_unit = to_value.get()

    from_factor = conversion_logic.get(from_unit, 1)
    to_factor = conversion_logic.get(to_unit, 1)
    result = (amount * from_factor) / to_factor

    result_label.config(text=f"Result: {result:.2f}")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

# make column 1 expand nicely
root.columnconfigure(1, weight=1)

# Title
main_label = tk.Label(root, text="Unit Converter", font=("Arial", 15))
main_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

# Amount
amount_label = tk.Label(root, text="Enter Amount:", font=("Arial", 15))
amount_label.grid(row=1, column=0, sticky='w', padx=10)

amount_input = tk.Entry(root, font=("Arial", 15))
amount_input.grid(row=1, column=1, sticky='ew', padx=10, pady=(0, 20))

# From
fromvalue_label = tk.Label(root, text="From:", font=("Arial", 15))
fromvalue_label.grid(row=2, column=0, sticky='w', padx=10)

from_value = ttk.Combobox(root, values=list(conversion_logic.keys()), state="readonly")
from_value.grid(row=2, column=1, sticky='ew', padx=10)

# To
tovalue_label = tk.Label(root, text="To:", font=("Arial", 15))
tovalue_label.grid(row=3, column=0, sticky='w', padx=10)

to_value = ttk.Combobox(root, values=list(conversion_logic.keys()), state="readonly")
to_value.grid(row=3, column=1, sticky='ew', padx=10)

# Button
convert_button = tk.Button(root, text="Convert", font=("Arial", 15), command=calculate_conversion)
convert_button.grid(row=4, column=0, columnspan=2, pady=20)

# Result
result_label = tk.Label(root, text="Result:", font=("Arial", 15))
result_label.grid(row=5, column=0, columnspan=2, pady=(0, 20))

def onclose():
    root.destroy()
    subprocess.run(["python", "main.py"])

root.protocol("WM_DELETE_WINDOW", onclose)

root.mainloop()