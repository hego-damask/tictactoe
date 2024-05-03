import os
import random
import math
from copy import deepcopy
def clear_screen(): os.system('clear||cls')

class Tictactoe:
    def __init__(self):
        self.board = [0 for i in range(9)]
        self.history = []
        self.n_moves = 0
    def __copy__(self):
        newone = type(self)()
        newone.__dict__.update(self.__dict__)
        return newone
    def __str__(self):
        symbol = lambda x: 'X' if x == 1 else 'O' if x == -1 else ' '
        board = f'{symbol(self.board[0])}|{symbol(self.board[1])}|{symbol(self.board[2])}\n{symbol(self.board[3])}|{symbol(self.board[4])}|{symbol(self.board[5])}\n{symbol(self.board[6])}|{symbol(self.board[7])}|{symbol(self.board[8])}\n'
        return board
    def reference(self):
        ref = [i for i in range(9)]
        print(f'{ref[0]}|{ref[1]}|{ref[2]}\n{ref[3]}|{ref[4]}|{ref[5]}\n{ref[6]}|{ref[7]}|{ref[8]}\n')
    def get_state(self): return ''.join(str(cell) for cell in self.board)
    def available_moves(self): return list(set(range(9)) - set(self.history))
    def check(self):
        #  1: player 1 wins | -1: player 2 wins | 3: game not completed | 0: draw
        if self.n_moves >= 5:
            s = self.board[0] + self.board[1] + self.board[2]
            if s == 3:
                return 1
            elif s == -3:
                return -1
            s = self.board[3] + self.board[4] + self.board[5]
            if s == 3:
                return 1
            elif s == -3:
                return -1
            s = self.board[6] + self.board[7] + self.board[8]
            if s == 3:
                return 1
            elif s == -3:
                return -1
            s = self.board[1] + self.board[4] + self.board[7]
            if s == 3:
                return 1
            elif s == -3:
                return -1
            s = self.board[2] + self.board[5] + self.board[8]
            if s == 3:
                return 1
            elif s == -3:
                return -1
            s = self.board[0] + self.board[3] + self.board[6]
            if s == 3:
                return 1
            elif s == -3:
                return -1
            s = self.board[0] + self.board[4] + self.board[8]
            if s == 3:
                return 1
            elif s == -3:
                return -1
            s = self.board[6] + self.board[4] + self.board[2]
            if s == 3:
                return 1
            elif s == -3:
                return -1

            if self.n_moves == 9:
                return 0
        return 3
    def move(self, choice, turn):
        #return code
        #  1 : player 1 wins
        # -1 : player 2 wins
        #  3 : game not done
        #  0 : draw
        #  4 : choice in history
        #  5 : choice not in range
        #assert(choice not in self.history)
        assert(choice in range(9))
        self.history.append(choice)
        self.n_moves += 1
        if turn:
            self.board[choice] = 1
        else:
            self.board[choice] = -1


class Game:
    def __init__(self):
        self.turn = 1
        self.board = Tictactoe()
    def content(self):
        clear_screen()
        print('Tictactoe')
        self.board.reference()
        print(self.board)
    def play(self):
        while True:
            self.content()
            choice = int(input(f'Player {self.turn}: '))
            self.board.move(choice, self.turn)
            result = self.board.check()
            if result == 3:
                self.turn = int(not(self.turn))
                continue
            elif result == 1:
                self.content()
                print('Player 1 wins')
                break
            elif result == -1:
                self.content()
                print('Player 2 wins')
                break
            elif result == 0:
                self.content()
                print('Draw')
                break
    def dumbAI(self):
        while True:
            self.content()
            print('dumb bot playing as "O"')
            if self.turn:
                choice = int(input(f'Player {self.turn}: '))
            else:
                choice = random.choice(list(set(range(9)) - set(self.board.history)))
            self.board.move(choice, self.turn)
            result = self.board.check()
            if result == 3:
                self.turn = int(not(self.turn))
                continue
            elif result == 1:
                self.content()
                print('Player 1 wins')
                break
            elif result == -1:
                self.content()
                print('dumb bot wins')
                break
            elif result == 0:
                self.content()
                print('Draw')
                break
    def smortAI(self):
        def minimax(board, depth, is_maximizing_player):
            result = board.check()
            if result == player:
                return 1
            elif result == -player:
                return -1
            elif result == 0:
                return 0
        
            if is_maximizing_player:
                best_score = -math.inf
                for move in board.available_moves():
                    new_board = deepcopy(board)
                    new_board.move(move, True)
                    score = minimax(new_board, depth + 1, False)
                    best_score = max(best_score, score)
                return best_score
            else:
                best_score = math.inf
                for move in board.available_moves():
                    new_board = deepcopy(board)
                    new_board.move(move, False)
                    score = minimax(new_board, depth + 1, True)
                    best_score = min(best_score, score)
                return best_score
        def get_best_move(board):
            best_move = None
            best_score = -math.inf
            for move in board.available_moves():
                new_board = deepcopy(board)
                new_board.move(move, True)
                score = minimax(new_board, 0, False)
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move
        player = 1
        while True:
            self.content()
            if self.turn:
                choice = get_best_move(self.board)
            else:
                choice = int(input(f'Player {self.turn}: '))
            self.board.move(choice, self.turn)
            result = self.board.check()
            if result == 3:
                self.turn = int(not(self.turn))
                continue
            elif result == 1:
                self.content()
                print('Player 1 wins')
                break
            elif result == -1:
                self.content()
                print('smort bot wins')
                break
            elif result == 0:
                self.content()
                print('Draw')
                break
g = Game()
g.smortAI()

