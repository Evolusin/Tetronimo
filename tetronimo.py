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
        self.rect.topleft = self.pos * TILE_SIZE


class Tetronimo:
    def __init__(self, tetris) -> None:
        self.tetris = tetris
        self.shape = random.choice(list(BLOCKS.keys()))
        self.blocks = [Block(self,pos) for pos in BLOCKS[self.shape]]
        pass

    def update(self):
        pass
