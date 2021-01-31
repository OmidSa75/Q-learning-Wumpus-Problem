import pygame
import random
from wumpus_world import Board, Game
from config import *


# def main():
#     return


if __name__ == '__main__':
    win = pygame.display.set_mode(BOARD_SIZE)
    pygame.display.set_caption('Wumpus World, Q learning')
    FPS = 60

    clock = pygame.time.Clock()
    game = Game(win, (0, 0), [(1, 2), (3, 4)], (2, 0), (4, 1))
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if game.end():
            run = False

        move_index = random.randint(0, 3)
        game.move(move_index)
        pygame.time.delay(1000)
        game.update()

