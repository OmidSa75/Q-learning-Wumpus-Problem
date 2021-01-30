import pygame
from config import *


class Board:
    def __init__(self, robot, holes, wumpus, gold):
        self.board = []
        self.holes = holes
        self.wumpus = wumpus
        self.gold = gold
        self.robot = robot

    def draw_squares(self, win):
        win.fill(WHITE)

        for row in range(ROWS):
            for col in range(COLUMNS):
                pygame.draw.rect(win, GRAY, (
                    row * SQUARE_SIZE + row * GAP, col * SQUARE_SIZE + col * GAP, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        pass

    def end_game(self):
        pass


class BoardGame:
    def __init__(self):
        self.board = None
