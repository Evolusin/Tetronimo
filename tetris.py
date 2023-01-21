from settings import *
import math
from tetronimo import Tetronimo

class Tetris:
    def __init__(self, app) -> None:
        self.app = app
        self.tetronimo = Tetronimo(self)

    def update(self):
        self.tetronimo.update()
        pass

    def draw(self):
        self.draw_grid()
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
