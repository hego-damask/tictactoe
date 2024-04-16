from array import array


def print_board(board):
    XO = lambda cell: 'X' if cell == 1 else 'O' if cell == -1 else ' '
    print(f'{XO(board[0])}|{XO(board[1])}|{XO(board[2])}') 
    print(f'{XO(board[3])}|{XO(board[4])}|{XO(board[5])}')
    print(f'{XO(board[6])}|{XO(board[7])}|{XO(board[8])}')
def check(board, choice):
    if choice == 0:
        


board = array('i', [0 for i in range(9)])
#print_board(board)
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
    if turn:
        board[choice] = 1
    else:
        board[choice] = -1
    turn = int(not(turn))
    n_moves += 1
    if n_moves >= 5:
        break
        result = check(board, choice)
        if result == 0:
            continue
        elif result == 1:
            print('Player 1 wins')
            break
        elif result == -1:
            print('Player 2 wins')
            break





