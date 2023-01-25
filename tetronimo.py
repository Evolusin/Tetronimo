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

    def is_coliding(self, pos):
        x, y = int(pos.x), int(pos.y)
        if (
            0 <= x < FIELD_W
            and y < FIELD_H
            and (y < 0 or not self.tetronimo.tetris.field_array[y][x])
        ):
            return False
        return True


class Tetronimo:
    def __init__(self, tetris) -> None:
        self.tetris = tetris
        self.shape = random.choice(list(BLOCKS.keys()))
        self.blocks = [Block(self, pos) for pos in BLOCKS[self.shape]]
        self.landing = False

    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        new_block_positions = [
            block.pos + move_direction for block in self.blocks
        ]
        is_colide = self.is_colliding(new_block_positions)

        if not is_colide:
            for block, pos in zip(self.blocks, new_block_positions):
                block.pos = pos
        elif direction == "DOWN":
            self.landing = True

    def is_colliding(self, block_position):
        return any(map(Block.is_coliding, self.blocks, block_position))

    def update(self):
        self.move(direction="DOWN")
