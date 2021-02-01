import random
import pygame
from utils import config ,Game, QLearning


if __name__ == '__main__':
    win = pygame.display.set_mode(config.BOARD_SIZE)
    pygame.display.set_caption('Wumpus World, Q learning')
    FPS = 60

    clock = pygame.time.Clock()
    game = Game(win, (0, 0), [(1, 2), (3, 4)], (2, 0), (4, 1))
    epsilon = 0.5
    alpha = 0.1
    gamma = 0.6
    q_learner = QLearning(gamma, alpha)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        state = game.board.robot

        if random.uniform(0, 1) < epsilon:
            move_index = random.randint(0, 3)
        else:
            move_index = q_learner.select_action(state)

        state = game.move(move_index)
        game.update()
        pygame.time.delay(1000)

        if game.end():
            break

