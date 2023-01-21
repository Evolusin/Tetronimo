from settings import *
import math
from tetronimo import Tetronimo
import pygame as pg

class Tetris:
    def __init__(self, app) -> None:
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetronimo = Tetronimo(self)

    def update(self):
        self.tetronimo.update()
        self.sprite_group.update()
        pass

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
        pass

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(
                    self.app.screen,
                    "black",
                    (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                    1,
                )
