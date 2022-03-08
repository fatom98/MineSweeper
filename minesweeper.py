# TODO: Flag win
# TODO: Question mark
# TODO: False flag
import pygame

from module.game import Game
from module.settings import FPS, WIN


def main():
    running = True
    clock = pygame.time.Clock()
    game = Game()

    while running:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
                game.handle_mouse(event)

        game.update(WIN)


if __name__ == '__main__':
    main()
