import pygame as pg
from settings import *


class Block(pg.sprite.Sprite):
    def __init__(self, tetronimo, pos) -> None:
        self.tetronimo = tetronimo

        super().__init__(tetronimo.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill("orange")

        self.rect = self.image.get_rect()
        self.rect.topleft = pos[0] * TILE_SIZE, pos[1] * TILE_SIZE


class Tetronimo:
    def __init__(self, tetris) -> None:
        self.tetris = tetris
        Block(self, (4, 5))
        pass

    def update(self):
        pass
