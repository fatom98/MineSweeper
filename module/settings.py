# TODO change screen size according to row col number
import pygame

from .sprite import Sprite

pygame.init()
display = pygame.display.Info()

SIZE = (WIDTH, HEIGHT) = display.current_w // 2, display.current_w // 2
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Minesweeper")

# Game Setup

ROWS = COLS = 25
MINE_COUNT = int(0.1488 * (ROWS ** 2) + 0.5655 * ROWS - 7.143)
SQUARE_SIZE = WIDTH // COLS
FPS = 60

# RGB Color
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (128, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
NAVY_BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

# Images
sprite = Sprite("spritesheet.jpg")

positions = []
for i in range(3):
    positions.extend((128 * j, 128 * i, 128, 128) for j in range(4))
TILE = pygame.transform.scale(sprite.get_sprite(positions[0], BLACK), (SQUARE_SIZE, SQUARE_SIZE))
FLAG = pygame.transform.scale(sprite.get_sprite(positions[1], WHITE), (SQUARE_SIZE, SQUARE_SIZE))
MINE = pygame.transform.scale(sprite.get_sprite(positions[2], WHITE), (SQUARE_SIZE, SQUARE_SIZE))
PRESSED = pygame.transform.scale(sprite.get_sprite(positions[3], BLACK), (SQUARE_SIZE, SQUARE_SIZE))
ONE = pygame.transform.scale(sprite.get_sprite(positions[4], BLACK), (SQUARE_SIZE, SQUARE_SIZE))
TWO = pygame.transform.scale(sprite.get_sprite(positions[5], BLACK), (SQUARE_SIZE, SQUARE_SIZE))
THREE = pygame.transform.scale(sprite.get_sprite(positions[6], BLACK), (SQUARE_SIZE, SQUARE_SIZE))
FOUR = pygame.transform.scale(sprite.get_sprite(positions[7], BLACK), (SQUARE_SIZE, SQUARE_SIZE))
FIVE = pygame.transform.scale(sprite.get_sprite(positions[8], BLACK), (SQUARE_SIZE, SQUARE_SIZE))
SIX = pygame.transform.scale(sprite.get_sprite(positions[9], BLACK), (SQUARE_SIZE, SQUARE_SIZE))
SEVEN = pygame.transform.scale(sprite.get_sprite(positions[10], BLACK), (SQUARE_SIZE, SQUARE_SIZE))
EIGHT = pygame.transform.scale(sprite.get_sprite(positions[11], BLACK), (SQUARE_SIZE, SQUARE_SIZE))

BOARD_PIECE = {
    "E": TILE,
    0: PRESSED,
    1: ONE,
    2: TWO,
    3: THREE,
    4: FOUR,
    5: FIVE,
    6: SIX,
    7: SEVEN,
    8: EIGHT,
    "M": MINE,
    "P": PRESSED,
    "F": FLAG
}
