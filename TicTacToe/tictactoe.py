import os
from pyfiglet import Figlet
import subprocess

f = Figlet(font='doom')


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

squares = [' ']*9
players = 'XO'
board = '''

    {0}|{1}|{2}
    -----
    {3}|{4}|{5}
    -----
    {6}|{7}|{8}


'''
win_conditions = [
    # Horizontal
    (0,1,2), (3,4,5), (6,7,8),
    # Vertical
    (0,3,6), (1,4,7), (2,5,8),
    # Diagonal
    (0,4,8), (2,4,6)
]
clear_console()

def check_win(player):
    for a, b, c in win_conditions:
        if {squares[a], squares[b], squares[c]} == {player}:
            return True
            

while True:
    print(board.format(*squares))
    if check_win(players[1]):
        print(f.renderText(f'{players[1]} is the winner!'))
        choice = input("Play again? (y/n): ").strip().lower()
        if choice == "y":
            subprocess.run(['python', 'TicTacToe/tictactoe.py'])
        else:
            subprocess.run(['python', 'main.py'])
            
    if ' ' not in squares:
        print('Cats game!')
        choice = input("Play again? (y/n): ").strip().lower()
        if choice == "y":
            subprocess.run(['python', 'TicTacToe/tictactoe.py'])
        else:
            subprocess.run(['python', 'main.py'])
    move = input(f'{players[0]} to move [0-8] ')
    if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ':
        print("Invalid move")
        continue
    squares[int(move)], players = players[0], players[::-1]
    clear_console()
