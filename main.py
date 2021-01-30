import pygame
from config import *


# def main():
#     return


if __name__ == '__main__':
    win = pygame.display.set_mode(BOARD_SIZE)
    pygame.display.set_caption('Wumpus World, Q learning')
    FPS = 60

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

