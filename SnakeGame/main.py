from pynput import keyboard
from pynput.keyboard import Key
import time, os, random
import subprocess

WIDTH, HEIGHT = 20, 10
direction = 'right'   # give it a starting direction so it moves immediately
pscore = 0

# snake is a list of (x, y) tuples, head is snake[0]
snake = [(5, 5), (4, 5), (3, 5)]

def random_food(snake):
    while True:
        pos = (random.randint(1, WIDTH - 1), random.randint(1, HEIGHT - 1))
        if pos not in snake:
            return pos

food = random_food(snake)

def on_press(key):
    global direction
    # prevent reversing directly into yourself
    if key == Key.up and direction != "down":
        direction = "up"
    elif key == Key.down and direction != "up":
        direction = "down"
    elif key == Key.left and direction != "right":
        direction = "left"
    elif key == Key.right and direction != "left":
        direction = "right"

listener = keyboard.Listener(on_press=on_press)
listener.start()

def reset_game():
    global snake, direction, pscore, food
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = 'right'
    pscore = 0
    food = random_food(snake)

def main():
    global food
    global pscore
    while True:
        head_x, head_y = snake[0]

        # compute new head position
        if direction == "up":
            new_head = (head_x, head_y - 1)
        elif direction == "down":
            new_head = (head_x, head_y + 1)
        elif direction == "left":
            new_head = (head_x - 1, head_y)
        elif direction == "right":
            new_head = (head_x + 1, head_y)
        else:
            new_head = (head_x, head_y)

        # check wall collision
        hit_wall = not (1 <= new_head[0] <= WIDTH - 1 and 1 <= new_head[1] <= HEIGHT - 1)
        # check self collision
        hit_self = new_head in snake

        if hit_wall or hit_self:
            print(f"Game Over, your score: {pscore}")
            match input("Would you like to play again? (y/n) "):
                case "y": 
                    reset_game()
                    continue
                case "n": 
                    subprocess.run(["python", "main.py"])
                    break
                case _: 
                    subprocess.run(['python', 'main.py'])
                    break

        snake.insert(0, new_head)  # move head forward

        if new_head == food:
            pscore += 1
            food = random_food(snake)
            # don't pop tail -> snake grows by one
        else:
            snake.pop()  # remove tail -> snake stays same length

        # rebuild the grid
        game_area = ''
        for y in range(1, HEIGHT):
            for x in range(1, WIDTH):
                pos = (x, y)
                if pos == snake[0]:
                    game_area += '@'          # head
                elif pos in snake:
                    game_area += 'o'          # body
                elif pos == food:
                    game_area += '*'          # food
                else:
                    game_area += '.'
            game_area += "\n"

        os.system('cls' if os.name == 'nt' else 'clear')
        print(game_area)
        print(f"Score: {pscore}")

        time.sleep(0.3)

def how_to_play():
    os.system('cls' if os.name == "nt" else 'clear')
    print("How to play\n1. Use arrow keys to move your snake (@ is your snakes head)\n2. Collect the *'s to get longer\n3. Get the longest snake you can")
    input("Press enter to return")
    nav()

def nav():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--NAVIGATION--\nPlease select one")
    print(
        """
1. Play
2. How to play
3. Exit
        """)

    try:
        num = int(input("Enter the number of the project you want to open: "))
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid input, try again")
        time.sleep(1.5)
        main()
        return

    match num:
        case 1: main()
        case 2: how_to_play()
        case 3: subprocess.run(['python', 'main.py'])

nav()