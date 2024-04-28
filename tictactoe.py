import os
import random
import pickle
import time
class Game:
    def __init__(self):
        self.board = [0 for i in range(9)]
        self.result = None
        self.qtable = dict()
        try:
            print('loading...')
            with open('bot.db', 'r') as db:
                lines = db.readlines()
                for line in lines:
                    k, v = line.split('|')
                    v = int(v[:-1])
                    if k in self.qtable.keys():
                        self.qtable[k].append(v)
                        self.qtable[k] = list(set(self.qtable[k]))
                    else:
                        self.qtable[k] = [v]
        except FileNotFoundError:
            print('db not found')
        time.sleep(0.5)

    def _reference(self):
        ref = [i for i in range(9)]
        print(f'{ref[0]}|{ref[1]}|{ref[2]}\n{ref[3]}|{ref[4]}|{ref[5]}\n{ref[6]}|{ref[7]}|{ref[8]}\n')
    def __str__(self):
        symbol = lambda x: 'X' if x == 1 else 'O' if x == -1 else ' '
        board = f'{symbol(self.board[0])}|{symbol(self.board[1])}|{symbol(self.board[2])}\n{symbol(self.board[3])}|{symbol(self.board[4])}|{symbol(self.board[5])}\n{symbol(self.board[6])}|{symbol(self.board[7])}|{symbol(self.board[8])}\n'
        return board
    def get_hash(self):
        board_hash = ''.join(str(i) for i in self.board) 
        return board_hash
    def _clear(self):
        os.system('cls||clear')
    def dumb_AI(self, history):
        board_hash = self.get_hash()
        roll = (random.choice(list(range(3))) != 0 )#33% random moves?
        if roll:
            if board_hash in self.qtable:
                move = self.qtable[board_hash]
                move = random.choice(move)
                if move not in history:
                    print('from db')
                    return move
            else:
                print('random bs')
                return random.choice(list(set(range(9))-set(history)))
        else:
            print('exploratory random bs')
            return random.choice(list(set(range(9))-set(history)))
    def _check(self, choice, n_moves):
        #  1: player 1 wins
        # -1: player 2 wins
        #  3: game not completed
        #  0: draw

        if n_moves == 9:
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
            return 0
        if n_moves >= 5:
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
        return 3
        

    def play(self):
        #self._clear()
        opp = int(input("Tic Tac Toe\n0)Human\n1)dumb AI\nPick your Op:"))
        assert opp in (0, 1)

        turn = 0
        history = [] #self or no self
        bot_moves = dict()
        player_moves = dict()
        n_moves = 0
        #self._clear()
        self._reference()
        print(self)
        if opp == 0:
            while True:
                choice = int(input(f'Player {turn+1}: '))
                if choice in history:
                    print('Choice already taken, pick another')
                    continue
                if choice not in range(9):
                    print('Pick a choice within range')
                    continue
                history.append(choice)

                if not(turn):
                    self.board[choice] = 1
                else:
                    self.board[choice] = -1
                n_moves += 1
                turn = int(not(turn))
                result = self._check(choice, n_moves)
                self._clear()
                self._reference()
                print(self)
                if result == 0:
                    print('Its a draw')
                    break
                elif result == 1:
                    print('Player 1 wins')
                    break
                elif result == -1:
                    print('Player 2 wins')
                    break


        elif opp == 1:
            #self._reference()
            while True:
                if not(turn):
                    choice = int(input("Your choice: "))
                    if choice in history:
                        print('Choice already taken, pick another')
                        continue
                    if choice not in range(9):
                        print('pick a choice within range dipshit')
                        continue
                    history.append(choice)
                    player_moves[str(self.get_hash())] = choice
                    self.board[choice] = 1
                else:
                    bot_choice = self.dumb_AI(history)
                    history.append(bot_choice)
                    #print(f'game state: {str(self.get_hash())}')
                    #print(f'bot choice: {bot_choice}')
                    bot_moves[str(self.get_hash())] = bot_choice
                    self.board[bot_choice] = -1
                n_moves += 1
                turn = int(not(turn))
                result = self._check(choice, n_moves)
                #self._clear()
                #self._reference()
                print(self)
                if result == 0:
                    print('Its a draw against the dumb AI')
                    return 0
                elif result == 1:
                    print('You win')
                    for state in player_moves:
                        with open('bot.db', 'a') as db:
                            db.write(f"{state}|{player_moves[state]}\n")
                    return 1
                elif result == -1:
                    print('You lost, lol')
                    for state in bot_moves:
                        with open('bot.db', 'a') as db:
                            db.write(f"{state}|{bot_moves[state]}\n")
                    return -1


g = Game()
g.play()


