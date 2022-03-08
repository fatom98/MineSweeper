import os

import pygame


class Sprite:

    def __init__(self, file_name):
        self.file_name = file_name
        self.sprite_sheet = pygame.image.load(os.path.join("assets", file_name)).convert()

    def get_sprite(self, pos, color_key):
        x, y, w, h = pos
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey(color_key)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite
