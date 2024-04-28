#!/usr/bin/python
from array import array

def print_board(board, num = False):
    XO = lambda cell: 'X' if cell == 1 else 'O' if cell == -1 else ' '
    result = ['' for i in range(9)]
    for i, cell in enumerate(board):
        if cell == 1:
            result[i] = 'X'
        elif cell == -1:
            result[i] = 'O'
        else:
            if num:
                result[i] = i
            else:
                result[i] = ' '
    print(f'{result[0]}|{result[1]}|{result[2]}') 
    print(f'{result[3]}|{result[4]}|{result[5]}')
    print(f'{result[6]}|{result[7]}|{result[8]}')

def check(board, choice):
    s = board[0] + board[1] + board[2]
    if s == 3:
        return 1
    elif s == -3:
        return -1

    s = board[3] + board[4] + board[5]
    if s == 3:
        return 1
    elif s == -3:
        return -1

    s = board[6] + board[7] + board[8]
    if s == 3:
        return 1
    elif s == -3:
        return -1

    s = board[1] + board[4] + board[7]
    if s == 3:
        return 1
    elif s == -3:
        return -1

    s = board[2] + board[5] + board[8]
    if s == 3:
        return 1
    elif s == -3:
        return -1

    s = board[0] + board[3] + board[6]
    if s == 3:
        return 1
    elif s == -3:
        return -1

    s = board[0] + board[4] + board[8]
    if s == 3:
        return 1
    elif s == -3:
        return -1

    s = board[6] + board[4] + board[2]
    if s == 3:
        return 1
    elif s == -3:
        return -1

    return 0

board = array('i', [0 for i in range(9)])
print_board(board, num = True)
print('='*6)
turn = 0
n_moves = 0
history = []
while(True):
    print_board(board)
    choice = int(input(f'Player {turn+1}: '))
    if choice not in range(9):
        print('Pick a choice between 0 and 8')
        continue
    elif choice in history:
        print('Choice already taken, pick another')
        continue
    history.append(choice)
    if not(turn):
        board[choice] = 1
    else:
        board[choice] = -1
    turn = int(not(turn))
    n_moves += 1
    if n_moves == 9:
        print('Its a draw')
        break
    if n_moves >= 5:
        result = check(board, choice)
        if result == 0:
            continue
        elif result == 1:
            print('Player 1 wins')
            break
        elif result == -1:
            print('Player 2 wins')
            break
    





