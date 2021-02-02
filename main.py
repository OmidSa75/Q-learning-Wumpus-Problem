import random
import pygame
from utils import config, Game, QLearning
import logging


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // config.SQUARE_SIZE
    col = x // config.SQUARE_SIZE
    return row, col


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(levelname)s:  %(message)s')
    win = pygame.display.set_mode(config.BOARD_SIZE)
    pygame.display.set_caption('Wumpus World, Q learning')
    FPS = 60

    clock = pygame.time.Clock()
    game = Game(win, (0, 0), [(1, 2), (3, 4)], (2, 0), (4, 1))
    '''HyperParameters'''
    epsilon = 0.95
    alpha = 0.1
    gamma = 0.9

    q_learner = QLearning(gamma, alpha)
    penalties = 0

    for epoch in range(1, 10000):
        game.reset((0, 4), [(1, 2), (3, 4)], (2, 0), (4, 1))
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            state = game.board.robot

            if random.uniform(0, 1) < epsilon:
                action = random.randint(0, 3)
            else:
                action = q_learner.select_action(state)

            next_state, reward, end = game.move(action)

            q_learner.optimize(state, action=action, next_state=next_state, reward=reward)

            if reward == -10:
                penalties += 1

            game.update()
            pygame.time.delay(1)

            if game.end():
                break

        if epoch % 100 == 0:
            logging.info(f"Epoch: {epoch}")
            epsilon *= 0.9
            alpha *= 0.9

            logging.info(f"Learning Rate : {alpha} | Epsilon : {epsilon}")
