from tictactoe import Tictactoe, clear_screen
from copy import deepcopy
import time
import random

def minimax(board, XO):
    if XO == 1:
        best = [None, -float('inf')]
    else:
        best = [None, float('inf')]
    result = board.check()
    if result in (1, 0, -1):
        score = result*(len(board.available_moves())+1)
        return [None, score]
    for move in board.available_moves():
        new_board = deepcopy(board)
        new_board.move(move, XO)
        _, score = minimax(new_board, -XO)
        if XO == 1:
            if score > best[1]:
                best = [move, score]
        else:
            if score < best[1]:
                best = [move, score]
    return best


if __name__ == '__main__':
    clear_screen()
    print('Welcome')
    go_first = input('Do you want to go first? [Y/n]: ').lower()
    if go_first in ('', 'y'):
        human = 1
        bot = -1
        turn = 1
    else:
        human = -1
        bot = 1
        turn = 0
    board = Tictactoe()
    history = []
    while True:
        clear_screen()
        board.reference()
        print(board)
        if len(history):
            if not turn:
                print(f'You played: {history[-1]}')
            else:
                print(f'Bot played: {history[-1]}')
        if turn:
            human_choice = int(input('Your choice: '))
            if human_choice not in range(9):
                print("pick a choice within range (0..8)")
                continue
            elif human_choice in history:
                print('choice already taken, pick another')
                continue
            history.append(human_choice)
            board.move(human_choice, human)
        else:
            if len(board.available_moves()) == 9:
                bot_choice = random.choice(range(9))
            else:
                bot_choice = minimax(board, bot)[0]
            history.append(bot_choice)
            board.move(bot_choice, bot)
        turn = int(not(turn))
        result = board.check()
        if result == 1:
            clear_screen()
            board.reference()
            print(board)
            if len(history):
                if not turn:
                    print(f'You played: {history[-1]}')
                else:
                    print(f'Bot played: {history[-1]}')
            print('X wins')
            break
        elif result == -1:
            clear_screen()
            board.reference()
            print(board)
            if len(history):
                if not turn:
                    print(f'You played: {history[-1]}')
                else:
                    print(f'Bot played: {history[-1]}')
            print('O wins')
            break
        elif result == 0:
            clear_screen()
            board.reference()
            print(board)
            if len(history):
                if not turn:
                    print(f'You played: {history[-1]}')
                else:
                    print(f'Bot played: {history[-1]}')
            print('Draw')
            break

