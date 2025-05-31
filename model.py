import numpy as np
from constants import Constants
BOARD_ROWS = Constants.BOARD_ROWS
BOARD_COLS = Constants.BOARD_COLS

class GameModel:
    def __init__(self):
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS), dtype=int)

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def available_square(self, row, col):
        return self.board[row][col] == 0

    def is_board_full(self):
        return np.all(self.board != 0)

    def check_win(self, player):
        # rows
        for r in range(BOARD_ROWS):
            if np.all(self.board[r, :] == player):
                return True, [(r, c) for c in range(BOARD_COLS)]
        # cols
        for c in range(BOARD_COLS):
            if np.all(self.board[:, c] == player):
                return True, [(r, c) for r in range(BOARD_ROWS)]
        # diagonals
        if (self.board[0,0]==player and self.board[1,1]==player and self.board[2,2]==player):
            return True, [(i, i) for i in range(BOARD_ROWS)]
        if (self.board[0,2]==player and self.board[1,1]==player and self.board[2,0]==player):
            return True, [(i, 2-i) for i in range(BOARD_ROWS)]
        return False, []

    def minimax(self, depth, is_maximizing):
        # simple minimax as before
        if self.check_win(2)[0]:
            return 1
        if self.check_win(1)[0]:
            return -1
        if self.is_board_full():
            return 0

        if is_maximizing:
            best = -np.inf
            for r in range(BOARD_ROWS):
                for c in range(BOARD_COLS):
                    if self.available_square(r, c):
                        self.board[r,c] = 2
                        score = self.minimax(depth+1, False)
                        self.board[r,c] = 0
                        best = max(best, score)
            return best
        else:
            best = np.inf
            for r in range(BOARD_ROWS):
                for c in range(BOARD_COLS):
                    if self.available_square(r, c):
                        self.board[r,c] = 1
                        score = self.minimax(depth+1, True)
                        self.board[r,c] = 0
                        best = min(best, score)
            return best

    def ai_move(self):
        best_score = -np.inf
        move = None
        for r in range(BOARD_ROWS):
            for c in range(BOARD_COLS):
                if self.available_square(r, c):
                    self.board[r,c] = 2
                    score = self.minimax(0, False)
                    self.board[r,c] = 0
                    if score > best_score:
                        best_score = score
                        move = (r, c)
        if move:
            self.mark_square(move[0], move[1], 2)
