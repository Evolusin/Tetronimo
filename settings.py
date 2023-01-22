import pygame as pg


vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32)

TILE_SIZE = 40
FIELD_SIZE = FIELD_W, FIELD_H = 10, 16
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

INIT_VEC_POS = vec(FIELD_SIZE) // 2

MOVE_DIRECTIONS = {"LEFT": vec(-1, 0), "RIGHT": vec(1, 0), "DOWN": vec(0, 1)}

BLOCKS = {
    "T": [(0, 0), (-1, 0), (1, 0), (0, -1)],
    "O": [(0, 0), (0, -1), (1, 0), (1, -1)],
    "J": [(0, 0), (-1, 0), (0, -1), (0, -2)],
    "L": [(0, 0), (1, 0), (0, -1), (0, -2)],
    "I": [(0, 0), (0, 1), (0, -1), (0, -2)],
    "S": [(0, 0), (-1, 0), (0, -1), (1, -1)],
    "Z": [(0, 0), (1, 0), (0, -1), (-1, -1)],
}
