import subprocess

def calculator():
    print("Simple calculator att.")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter Operator: ")
        num2 = float(input("Enter second number: "))

        equation = f'{num1} {operator} {num2}'
        result = eval(equation)

        print("Your answer is", result)
    except ValueError:
        print("Invalid Input")

calculator()

choice = input("Exit? (y/n): ").strip().lower()
if choice == "y":
    subprocess.run(['python', 'main.py'])
else: subprocess.run(['python', 'Calculator/calculator.py'])