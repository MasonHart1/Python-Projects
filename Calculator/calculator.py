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

choice = input("Exit? (yes or no): ").strip().lower()
if choice == "yes":
    subprocess.run(['python', 'Python Projects/main.py'])
else: subprocess.run(['python', 'Python Projects/Calculator/calculator.py'])