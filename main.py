import random
import pygame
from utils import config, Game, QLearning
import logging
import argparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(levelname)s:  %(message)s')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // config.SQUARE_SIZE
    col = x // config.SQUARE_SIZE
    return row, col


def main(opt):
    win = pygame.display.set_mode(config.BOARD_SIZE)
    pygame.display.set_caption('Wumpus World, Q learning')
    FPS = 60

    clock = pygame.time.Clock()
    game = Game(win, None, None, None, None)

    items = {"robot": None, "wumpus": None, "hole1": None, "hole2": None, "gold": None}
    for i, item in enumerate(items.keys()):
        run = True
        logging.info(f"***SELECT {item}***")
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)

                    items[item] = (col, row)
                    run = False
                    break

            game.reset(items['robot'], [items['hole1'], items['hole2']], items['wumpus'], items['gold'])
            game.update()

    '''HyperParameters'''
    epsilon = opt.epsilon
    alpha = opt.lr
    gamma = opt.gamma

    q_learner = QLearning(gamma, alpha)
    penalties = 0

    logging.info(f"\n\n{40 * '*'} start learning {40 * '*'}\n\n")
    for epoch in range(1, opt.num_epochs+1):
        game.reset(items['robot'], [items['hole1'], items['hole2']], items['wumpus'], items['gold'])
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

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
            logging.info(f"Epoch: {epoch}, Penalties: {penalties}")
            if opt.decay:
                epsilon *= 0.9
                q_learner.alpha *= 0.9

                logging.info(f"Learning Rate : {q_learner.alpha} | Epsilon : {epsilon}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--epsilon', type=float, default=0.95)
    parser.add_argument('--lr', type=float, default=0.1, help="learning rate")
    parser.add_argument('--gamma', type=float, default=0.9, help="discount factor")
    parser.add_argument('--num_epochs', type=int, default=10000, help="Number of epochs")
    parser.add_argument('--decay', action='store_true', default=True,
                        help="If true, The learning rate and epsilon will be decrease during iterations")

    opt = parser.parse_args()
    main(opt)

