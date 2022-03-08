import pygame

from .board import Board
from .settings import WHITE, SQUARE_SIZE


class Game:

    def __init__(self):
        self.board = Board()

    def update(self, win):
        win.fill(WHITE)
        self.board.draw(win)
        pygame.display.update()

    def handle_mouse(self, event):
        event_type = event.type
        x, y = event.pos
        r = y // SQUARE_SIZE
        c = x // SQUARE_SIZE

        button = self.board.get_disp(r, c)

        if button.pressed:

            if event.button == 3:

                if button.value == "F" or button.value == "P":

                    if event_type == pygame.MOUSEBUTTONDOWN:
                        self.board.set_disp(r, c, "P")

                    elif event_type == pygame.MOUSEBUTTONUP:
                        button.un_press()
                        self.board.set_disp(r, c, "E")

        else:

            if event.button == 1:

                if event_type == pygame.MOUSEBUTTONDOWN:
                    self.board.set_disp(r, c, "P")

                elif event_type == pygame.MOUSEBUTTONUP:
                    button.press()
                    button = self.board.get_board(r, c)

                    if button.value != 0:

                        if button.value == "M":
                            self.finish()

                        self.board.set_disp(r, c, button.value)

                    else:
                        self.board.reveal(button)
                        self.board.check.clear()

            elif event.button == 3:
                if event_type == pygame.MOUSEBUTTONDOWN:

                    self.board.set_disp(r, c, "P")

                elif event_type == pygame.MOUSEBUTTONUP:

                    button.press()
                    self.board.set_disp(r, c, "F")

    def finish(self):
        self.board.finished = True
