from settings import *
import math
from tetronimo import Tetronimo
import pygame as pg


class Tetris:
    def __init__(self, app) -> None:
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetronimo = Tetronimo(self)

    def get_field_array(self):
        # This function returns an empty field, initialized with zeros.
        # The field has FIELD_H rows and FIELD_W columns.
        # The function iterates through every row and column, and sets
        # the field value for that row and column to zero.
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def put_tetronimo_blocks_in_array(self):
        for block in self.tetronimo.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def check_landing(self):
        if self.tetronimo.landing:
            self.put_tetronimo_blocks_in_array()
            self.tetronimo = Tetronimo(self)

    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetronimo.move("LEFT")
        elif pressed_key == pg.K_RIGHT:
            self.tetronimo.move("RIGHT")
        elif pressed_key == pg.K_SPACE:
            self.tetronimo.rotate_tetronimo()

    def update(self):
        if self.app.anim_triger:
            self.tetronimo.update()
            self.check_landing()
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
