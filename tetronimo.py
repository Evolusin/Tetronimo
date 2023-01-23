import pygame as pg
from settings import *
import random


class Block(pg.sprite.Sprite):
    def __init__(self, tetronimo, pos) -> None:
        self.tetronimo = tetronimo
        self.pos = vec(pos) + INIT_VEC_POS

        super().__init__(tetronimo.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill("orange")

        self.rect = self.image.get_rect()

    def rect_update(self):
        self.rect.topleft = self.pos * TILE_SIZE

    def update(self):
        self.rect_update()


class Tetronimo:
    def __init__(self, tetris) -> None:
        self.tetris = tetris
        self.shape = random.choice(list(BLOCKS.keys()))
        self.blocks = [Block(self, pos) for pos in BLOCKS[self.shape]]

    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        for block in self.blocks:
            block.pos += move_direction

    def update(self):
        self.move(direction="DOWN")
