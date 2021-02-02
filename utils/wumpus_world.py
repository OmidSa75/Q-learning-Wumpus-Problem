import numpy as np
from utils.config import *


class Board:
    def __init__(self, robot, holes, wumpus, gold):
        self.board = np.zeros((ROWS, COLUMNS))
        self.holes = holes
        self.wumpus = wumpus
        self.gold = gold
        self.robot = robot

    def draw(self, win):
        self.draw_squares(win)
        self.draw_holes(win)
        self.draw_gold(win)
        self.draw_wumpus(win)
        self.draw_agent(win)

    def draw_squares(self, win):
        win.fill(GRAY)

        for row in range(ROWS):
            for col in range(COLUMNS):
                pygame.draw.rect(win, WHITE, (
                    row * SQUARE_SIZE + row * GAP, col * SQUARE_SIZE + col * GAP, SQUARE_SIZE, SQUARE_SIZE))

    def draw_holes(self, win):
        if self.holes:
            for hole in self.holes:
                if hole:
                    pygame.draw.rect(win, BLACK, (hole[0] * SQUARE_SIZE + hole[0] * GAP,
                                                  hole[1] * SQUARE_SIZE + hole[1] * GAP,
                                                  SQUARE_SIZE,
                                                  SQUARE_SIZE))

                    win.blit(FONT.render('PIT', True, (0, 255, 255)),
                             ((hole[0] * SQUARE_SIZE + hole[0] * GAP) + SQUARE_SIZE // 2 - FONT.get_linesize()//2,
                              (hole[1] * SQUARE_SIZE + hole[1] * GAP) + SQUARE_SIZE // 2 - FONT.get_linesize()//2))

    def draw_agent(self, win):
        if self.robot:
            agent = self.robot
            win.blit(ROBOT, (agent[0] * SQUARE_SIZE + ROBOT.get_width() // 2,
                             agent[1] * SQUARE_SIZE + ROBOT.get_height() // 2))

    def draw_gold(self, win):
        if self.gold:
            gold = self.gold
            win.blit(GOLD, (gold[0] * SQUARE_SIZE + GOLD.get_width() // 2,
                            gold[1] * SQUARE_SIZE + GOLD.get_height() // 2))

    def draw_wumpus(self, win):
        if self.wumpus:
            wumpus = self.wumpus
            win.blit(WUMPUS, (wumpus[0] * SQUARE_SIZE + WUMPUS.get_width() // 2,
                              wumpus[1] * SQUARE_SIZE + WUMPUS.get_height() // 2))

    def move(self, move_index):
        moves = self.get_valid_moves()
        # print("Move index: {} | Moves : {}".format(move_index, moves))
        if moves[move_index]:
            self.robot = moves[move_index]
        else:
            return False

    def end_game(self):
        good = [self.gold]
        bad = [self.wumpus, *self.holes]
        if self.robot in good:
            return True
        elif self.robot in bad:
            return True
        else:
            return False

    def get_valid_moves(self):
        left = (self.robot[0] - 1, self.robot[1])
        right = (self.robot[0] + 1, self.robot[1])
        up = (self.robot[0], self.robot[1] - 1)
        down = (self.robot[0], self.robot[1] + 1)

        moves = [left, right, up, down]
        valid_moves = []
        for x, y in moves:
            if (0 <= x < 5) and (0 <= y < 5):
                valid_moves.append((x, y))
            else:
                valid_moves.append(False)

        return valid_moves

    def reward(self):
        good = [self.gold]
        bad = [self.wumpus, *self.holes]

        if self.robot in bad:
            return -100
        elif self.robot in good:
            return 100
        else:
            return 1


class Game:
    def __init__(self, win, robot, holes, wumpus, gold):
        self._init(robot, holes, wumpus, gold)
        self.win = win

    def _init(self, robot, holes, wumpus, gold):
        self.board = Board(robot, holes, wumpus, gold)

    def reset(self, robot, holes, wumpus, gold):
        self._init(robot, holes, wumpus, gold)

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def move(self, move_index):
        self.board.move(move_index)
        reward = self.board.reward()
        end = self.board.end_game()

        return self.board.robot, reward, end

    def end(self):
        return self.board.end_game()
