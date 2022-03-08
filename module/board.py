import random

from .button import Button
from .settings import ROWS, COLS, MINE_COUNT, BOARD_PIECE, SQUARE_SIZE


class Board:

    def __init__(self):
        self.check = []
        self.board = []
        self.disp = []
        self.mines = []
        self.finished = False
        self.create()

    def create(self):

        for row in range(ROWS):
            self.board.append([])
            self.disp.append([])

            for col in range(COLS):
                self.board[row].append(Button(row, col, "E"))
                self.disp[row].append(Button(row, col, "E"))

        for _ in range(MINE_COUNT):

            while True:
                row = random.randint(0, ROWS - 1)
                col = random.randint(0, COLS - 1)
                pos = (row, col)

                if pos not in self.mines:
                    self.mines.append(pos)
                    break

        for row, col in self.mines:
            piece = self.board[row][col]
            piece.value = "M"

        for row in range(ROWS):
            for col in range(COLS):

                current = self.board[row][col]

                if current.value != "M":

                    score = 0

                    moves = [
                        (row - 1, col),  # up
                        (row - 1, col + 1),  # up_right
                        (row, col + 1),  # right
                        (row + 1, col + 1),  # down_right
                        (row + 1, col),  # down
                        (row + 1, col - 1),  # down_left
                        (row, col - 1),  # left
                        (row - 1, col - 1)  # up_left
                    ]

                    for r, c in moves:

                        if (0 <= r < ROWS) and (0 <= c < COLS):

                            piece = self.board[r][c]

                            if piece.value == "M":
                                score += 1

                    self.board[row][col].value = score

    def draw(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                button = self.disp[row][col] if not self.finished else self.board[row][col]
                win.blit(BOARD_PIECE[button.value], (col * SQUARE_SIZE, row * SQUARE_SIZE))

    def set_disp(self, row, col, to):
        self.disp[row][col].value = to

    def get_disp(self, row, col):
        return self.disp[row][col]

    def get_board(self, row, col):

        if (0 <= row < ROWS) and (0 <= col < COLS):
            return self.board[row][col]

        else:
            return None

    def reveal(self, button):
        row = button.row
        col = button.col
        value = button.value

        if value == 0:

            self.set_disp(row, col, 0)

            moves = [
                (row - 1, col),  # up
                (row - 1, col + 1),  # up_right
                (row, col + 1),  # right
                (row + 1, col + 1),  # down_right
                (row + 1, col),  # down
                (row + 1, col - 1),  # down_left
                (row, col - 1),  # left
                (row - 1, col - 1)  # up_left
            ]

            for r, c in moves:
                if (r, c) not in self.check:
                    self.check.append((r, c))
                    if b := self.get_board(r, c):
                        self.reveal(b)

        elif value != "M":
            self.set_disp(row, col, value)
