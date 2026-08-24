import random
import os
import time
import subprocess
import keyboard

def exit():
    print("Exiting", end="", flush=True)
    for i in range(3):
        time.sleep(.75)
        print(".", end="", flush=True)
    print()
    time.sleep(.5)
    subprocess.run(["python", "main.py"])

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def how_to_play():
    clear_console()
    print(
        "How to play:\n"
        "1. Choose a category from the main menu.\n"
        "2. Answer the questions by typing the number corresponding to your answer (1-4).\n"
        "3. Your score will be displayed at the end of the game.\n"
        "4. You can choose to play again or select a new category.\n"
    )
    print("Press any key to return to the main menu...")
    keyboard.read_key(suppress=True)
    main()

general_knowledge = {
    "What is the largest ocean on Earth?": {
        "correct_answer": "Pacific Ocean",
        "wrong_answers": ["Atlantis Ocean", "Indian Ocean", "Arctic Ocean"]
    },
    "How many continents are there?": {
        "correct_answer": "7",
        "wrong_answers": ["5", "6", "8"]
    },
    "What is the smallest country in the world?": {
        "correct_answer": "Vatican City",
        "wrong_answers": ["Monaco", "San Marino", "Liechtenstein"]
    },
    "What is the hardest natural substance on Earth?": {
        "correct_answer": "Diamond",
        "wrong_answers": ["Gold", "Iron", "Quartz"]
    },
    "How many sides does a hexagon have?": {
        "correct_answer": "6",
        "wrong_answers": ["5", "7", "8"]
    },
    "What is the currency of Japan?": {
        "correct_answer": "Yen",
        "wrong_answers": ["Won", "Yuan", "Rupee"]
    },
    "What is the fastest land animal?": {
        "correct_answer": "Cheetah",
        "wrong_answers": ["Lion", "Horse", "Leopard"]
    },
    "How many degrees are in a circle?": {
        "correct_answer": "360",
        "wrong_answers": ["180", "90", "270"]
    },
    "What is the largest mammal in the world?": {
        "correct_answer": "Blue Whale",
        "wrong_answers": ["Elephant", "Giraffe", "Orca"]
    },
    "What country has the Eiffel Tower?": {
        "correct_answer": "France",
        "wrong_answers": ["Italy", "Spain", "Germany"]
    }
}

geography = {
    # 1
    "What continent is the Sahara Desert located in?": {
        "correct_answer": "Africa",
        "wrong_answers": ["Asia", "Australia", "South America"]
    },
    # 2
    "What is the capital of Australia?": {
        "correct_answer": "Canberra",
        "wrong_answers": ["Sydney", "Melbourne", "Brisbane"]
    },
    # 3
    "Which river is the longest in the world?": {
        "correct_answer": "Nile",
        "wrong_answers": ["Amazon", "Yangtze", "Mississippi"]
    },
    # 4
    "What is the biggest continent by land area?": {
        "correct_answer": "Asia",
        "wrong_answers": ["Africa", "North America", "Europe"]
    },
    # 5
    "What is the only country without red white or blue in their flag?": {
        "correct_answer": "Jamaica",
        "wrong_answers": ["Brazil", "South Africa", "India"]
    },
    # 6
    "What is the only country to have a non rectangular flag?": {
        "correct_answer": "Nepal",
        "wrong_answers": ["Switzerland", "Bhutan", "Malawi"]
    },
    # 7
    "Where was Aang found after 100 years?": {
        "correct_answer": "The South Pole",
        "wrong_answers": ["Ba Sing Se", "The North Pole", "The fire islands"]
    },
    # 8
    "What is the largest desert in the world?": {
        "correct_answer": "The Antarctic Desert",
        "wrong_answers": ["The Sahara Desert", "The Gobi Desert", "The Mojave Desert"]
    },
    # 9
    "What country has the most natural lakes": {
        "correct_answer": "Canada",
        "wrong_answers": ["The United States", "Portugal", "Sweden"]
    },
    # 10
    "What country is completely surrounded by South Africa?": {
        "correct_answer": "Lesotho",
        "wrong_answers": ["Nigeria", "Sudan", "Ghana"]
    }
}

science = {
    "What planet is known as the Red Planet?": {
        "correct_answer": "Mars",
        "wrong_answers": ["Earth", "Jupiter", "Saturn"]
    },

    "What is the chemical symbol for water?": {
        "correct_answer": "H2O",
        "wrong_answers": ["O2", "H", "CO2"]
    },
    "How many planets are in our solar system?": {
        "correct_answer": "8",
        "wrong_answers": ["7", "9", "10"]
    },
    "What gas do humans need to breathe?": {
        "correct_answer": "Oxygen",
        "wrong_answers": ["Carbon Dioxide", "Nitrogen", "Hydrogen"]
    },
    "What force keeps objects on the ground?": {
        "correct_answer": "Gravity",
        "wrong_answers": ["Magnetism", "Inertia", "Friction"]
    },
    "What is the largest planet in our solar system?": {
        "correct_answer": "Jupiter",
        "wrong_answers": ["Saturn", "Neptune", "Uranus"]
    },
    "What is the chemical symbol for gold?": {
        "correct_answer": "Au",
        "wrong_answers": ["Ag", "Pb", "Fe"]
    },
    "How many bones are in the human body?": {
        "correct_answer": "206",
        "wrong_answers": ["200", "210", "198"]
    },
    "What organ pumps blood throughout the body?": {
        "correct_answer": "Heart",
        "wrong_answers": ["Lungs", "Liver", "Kidneys"]
    },
    "What is the closest star to Earth?": {
        "correct_answer": "Sun",
        "wrong_answers": ["Proxima Centauri", "Alpha Centauri", "Betelgeuse"]
    }
}

programming = {
    # 1
    "How do you send something to the console in python?": {
        "correct_answer": "print()",
        "wrong_answers": ["console.log()", "Debug.Log()", "Console.WriteLine()"]
    },
    # 2
    "How do you make a function in python?": {
        "correct_answer": "def function_name()",
        "wrong_answers": ["function function_name()", "public void function_name()", "func function_name()"]
    },
    # 3
    "How do you store an int value in python?": {
        "correct_answer": "value = 1",
        "wrong_answers": ["int = 1", "int value = 1", "value = int 1"]
    },
    # 4
    "What is the ouput of this code? print(list(map(lambda x: x * 2, [1, 2, 3])))": {
        "correct_answer": "[2, 4, 6]",
        "wrong_answers": ["[1, 2, 3]", "[3, 6, 9]", "[4, 8, 12]"]
    },
    # 5
    "What would be the output of print(a == b) if a = [1, 2, 3] and b = [1, 2, 3]": {
        "correct_answer": "True",
        "wrong_answers": ["False", "[1, 2, 3]", "Error"]
    },
    # 6
    "What would the output of print(a is b) if a = [1, 2, 3] and b = [1, 2, 3]": {
        "correct_answer": "False",
        "wrong_answers": ["True"]
    },
    # 7
    "What is the language that makes a website look good?": {
        "correct_answer": "CSS",
        "wrong_answers": ["Javascript", "Python", "C#"]
    },
    # 8
    "What does list.append(item) do?": {
        "correct_answer": "Add the item to the end of the list",
        "wrong_answers": ["Adds the item to the beginning of the list", "Removes the item from the list", "Moves the item up 1 spot in a list"]
    },
    # 9
    "What does this print: print([x for x in range(10) if x % 2 == 0])": {
        "correct_answer": "All even numbers from 1-10",
        "wrong_answers": ["All odd numbers from 1-10", "Nothing", "Error"]
    },
    # 10
    "What does this print: print(list(enumerate(['apple', 'banana', 'cherry'])))": {
        "correct_answer": "[(0, 'apple'), (1, 'banana'), (2, 'cherry')]",
        "wrong_answers": ["[0, 1, 2]", "[(1, 'apple'), (2, 'banana'), (3, 'cherry')]", "['apple', 'banana', 'cherry']"]
    }
}

math = {
    # 1
    "What is 5 * 25": {
        "correct_answer": "125",
        "wrong_answers": ["120", "115", "100"]
    },
    # 2
    "Solve for x: 3x + 7 = 10": {
        "correct_answer": "x = 1",
        "wrong_answers": ["x = 2", "x = 3", "x = 4"]
    },
    # 3
    "What is the value of 5 + 3 * (8 - 2)?": {
        "correct_answer": "23",
        "wrong_answers": ["48", "19", "26"]
    },
    # 4
    "Solve for x: 3x - 4 = 11": {
        "correct_answer": "5",
        "wrong_answers": ["3", "4", "7"]
    },
    # 5
    "If two angles of a triangle are 50° and 70°, what is the measure of the third angle": {
        "correct_answer": "60°",
        "wrong_answers": ["80°", "70°", "90°"]
    },
    # 6
    "What is the sum of 3/4 and 1/2?": {
        "correct_answer": "1.25",
        "wrong_answers": ["1", "1.5", "1.75"]
    },
    # 7
    "if a = 3 and b = 5, what is the value of 2a² + b": {
        "correct_answer": "23",
        "wrong_answers": ["35", "30", "17"]
    },
    # 8
    "A rectangle has a length of 8 cm and a width of 5 cm. What is its area?": {
        "correct_answer": "40 cm²",
        "wrong_answers": ["13 cm²", "15 cm²", "26 cm²"]
    },
    # 9
    "What is 15% of 80?": {
        "correct_answer": "12",
        "wrong_answers": ["10", "15", "18"]
    },
    # 10
    "Simplify the expression: x^5 * x^3": {
        "correct_answer": "x^8",
        "wrong_answers": ["x^15", "x^2", "x^(5/3)"]
    }
}

def general_knowledge_game():
    correct_answers = 0
    questions = list(general_knowledge.keys())

    shuffled_questions = random.sample(questions, len(questions))

    for i, question in enumerate(shuffled_questions, 1):
        clear_console()
        correct_ans = general_knowledge[question]["correct_answer"]
        wrong_ans = general_knowledge[question]["wrong_answers"]

        answers = [correct_ans] + wrong_ans
        random.shuffle(answers)

        print(f"Question {i}/{len(shuffled_questions)}: {question} (answer with 1-4)")
        for i, answer in enumerate(answers, 1):
            print(f"{i}. {answer}")

        while True:
            try:
                user_answer = int(input("Your answer (type 0 for main menu): "))
                if user_answer == 0:
                    main()
                if user_answer < 1 or user_answer > 4:
                    raise ValueError
                if answers[user_answer - 1].lower() == correct_ans.lower():
                    print("Correct!")
                    correct_answers += 1
                else:
                    print(f"Wrong! The correct answer is: {correct_ans}")
                break
            except ValueError:
                print("Incorrect input")
        time.sleep(1.5)

    print(f"Game over! You got {correct_answers}/{len(shuffled_questions)} questions correct.")
    end_choice = input("Would you like to play again? (y/n): ").strip().lower()
    if end_choice == "y":
        general_knowledge_game()
    elif end_choice == "n":
        clear_console()
        choice2 = input("Would you like to try a new category? (y/n): ").strip().lower()
        if choice2 == "y":
            main()
        elif choice2 == "n":
            exit()

def science_game():
    correct_answers = 0
    questions = list(science.keys())

    shuffled_questions = random.sample(questions, len(questions))

    for i, question in enumerate(shuffled_questions, 1):
        clear_console()
        correct_ans = science[question]["correct_answer"]
        wrong_ans = science[question]["wrong_answers"]

        answers = [correct_ans] + wrong_ans
        random.shuffle(answers)

        print(f"Question {i}/{len(shuffled_questions)}: {question} (answer with 1-4)")
        for i, answer in enumerate(answers, 1):
            print(f"{i}. {answer}")

        while True:
            try:
                user_answer = int(input("Your answer (type 0 for main menu): "))
                if user_answer == 0:
                    main()
                if user_answer < 1 or user_answer > 4:
                    raise ValueError
                if answers[user_answer - 1].lower() == correct_ans.lower():
                    print("Correct!")
                    correct_answers += 1
                else:
                    print(f"Wrong! The correct answer is: {correct_ans}")
                break
            except ValueError:
                print("Incorrect input")
        time.sleep(1.5)

    print(f"Game over! You got {correct_answers}/{len(shuffled_questions)} questions correct.")
    end_choice = input("Would you like to play again? (y/n): ").strip().lower()
    if end_choice == "y":
        science_game()
    elif end_choice == "n":
        clear_console()
        choice2 = input("Would you like to try a new category? (y/n): ").strip().lower()
        if choice2 == "y":
            main()
        elif choice2 == "n":
            exit()

def programming_game():
    correct_answers = 0
    questions = list(programming.keys())

    shuffled_questions = random.sample(questions, len(questions))

    for i, question in enumerate(shuffled_questions, 1):
        clear_console()
        correct_ans = programming[question]["correct_answer"]
        wrong_ans = programming[question]["wrong_answers"]

        answers = [correct_ans] + wrong_ans
        random.shuffle(answers)

        print(f"Question {i}/{len(shuffled_questions)}: {question} (answer with 1-4)")
        for i, answer in enumerate(answers, 1):
            print(f"{i}. {answer}")

        while True:
            try:
                user_answer = int(input("Your answer (type 0 for main menu): "))
                if user_answer == 0:
                    main()
                if user_answer < 1 or user_answer > 4:
                    raise ValueError
                if answers[user_answer - 1].lower() == correct_ans.lower():
                    print("Correct!")
                    correct_answers += 1
                else:
                    print(f"Wrong! The correct answer is: {correct_ans}")
                break
            except ValueError:
                print("Incorrect input")
        time.sleep(1.5)

    print(f"Game over! You got {correct_answers}/{len(shuffled_questions)} questions correct.")
    end_choice = input("Would you like to play again? (y/n): ").strip().lower()
    if end_choice == "y":
        programming_game()
    elif end_choice == "n":
        clear_console()
        choice2 = input("Would you like to try a new category? (y/n): ").strip().lower()
        if choice2 == "y":
            main()
        elif choice2 == "n":
            exit()

def math_game():
    correct_answers = 0
    questions = list(math.keys())

    shuffled_questions = random.sample(questions, len(questions))

    for i, question in enumerate(shuffled_questions, 1):
        clear_console()
        correct_ans = math[question]["correct_answer"]
        wrong_ans = math[question]["wrong_answers"]

        answers = [correct_ans] + wrong_ans
        random.shuffle(answers)

        print(f"Question {i}/{len(shuffled_questions)}: {question} (answer with 1-4)")
        for i, answer in enumerate(answers, 1):
            print(f"{i}. {answer}")

        while True:
            try:
                user_answer = int(input("Your answer (type 0 for main menu): "))
                if user_answer == 0:
                    main()
                if user_answer < 1 or user_answer > 4:
                    raise ValueError
                if answers[user_answer - 1].lower() == correct_ans.lower():
                    print("Correct!")
                    correct_answers += 1
                else:
                    print(f"Wrong! The correct answer is: {correct_ans}")
                break
            except ValueError:
                print("Incorrect input")
        time.sleep(1.5)

    print(f"Game over! You got {correct_answers}/{len(shuffled_questions)} questions correct.")
    end_choice = input("Would you like to play again? (y/n): ").strip().lower()
    if end_choice == "y":
        math_game()
    elif end_choice == "n":
        clear_console()
        choice2 = input("Would you like to try a new category? (y/n): ").strip().lower()
        if choice2 == "y":
            main()
        elif choice2 == "n":
            exit()


def geography_game():
    correct_answers = 0
    questions = list(geography.keys())

    shuffled_questions = random.sample(questions, len(questions))

    for i, question in enumerate(shuffled_questions, 1):
        clear_console()
        correct_ans = geography[question]["correct_answer"]
        wrong_ans = geography[question]["wrong_answers"]

        answers = [correct_ans] + wrong_ans
        random.shuffle(answers)

        print(f"Question {i}/{len(shuffled_questions)}: {question} (answer with 1-4)")
        for i, answer in enumerate(answers, 1):
            print(f"{i}. {answer}")

        while True:
            try:
                user_answer = int(input("Your answer (type 0 for main menu): "))
                if user_answer == 0:
                    main()
                if user_answer < 1 or user_answer > 4:
                    raise ValueError
                if answers[user_answer - 1].lower() == correct_ans.lower():
                    print("Correct!")
                    correct_answers += 1
                else:
                    print(f"Wrong! The correct answer is: {correct_ans}")
                break
            except ValueError:
                print("Incorrect input")
        time.sleep(1.5)

    print(f"Game over! You got {correct_answers}/{len(shuffled_questions)} questions correct.")
    end_choice = input("Would you like to play again? (y/n): ").strip().lower()
    if end_choice == "y":
        geography_game()
    elif end_choice == "n":
        clear_console()
        choice2 = input("Would you like to try a new category? (y/n): ").strip().lower()
        if choice2 == "y":
            main()
        elif choice2 == "n":
            exit()


def main():
    clear_console()
    print("-----Welcome to my quiz game-----")
    menu = """
    1. General Knowledge
    2. Science
    3. Geography
    4. Programming
    5. Math
    6. How to play
    7. Exit
    """
    choice = input(menu)

    match choice:
        case "1":
            general_knowledge_game()
        case "2":
            science_game()
        case "3":
            geography_game()
        case "4":
            programming_game()
        case "5":
            math_game()
        case "6":
            how_to_play()
        case "7":
            exit()
        case _:
            print("Invalid choice. Please select a valid category.")
            time.sleep(1)
            main()

main()