import pygame

BOARD_SIZE = (516, 516)
GAP = 4
ROWS = 5
COLUMNS = 5
NUM_MOVES = 4
SQUARE_SIZE = 100

GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.font.init()
FONT = pygame.font.SysFont('rekha', 20)

WUMPUS = pygame.transform.scale(pygame.image.load('images/wumpus.png'),
                                (int(SQUARE_SIZE * 2 / 3), int(SQUARE_SIZE * 2 / 3)))
ROBOT = pygame.transform.scale(pygame.image.load('images/agent.png'),
                               (int(SQUARE_SIZE * 2 / 3), int(SQUARE_SIZE * 2 / 3)))
GOLD = pygame.transform.scale(pygame.image.load('images/gold.png'),
                              (int(SQUARE_SIZE * 2 / 3), int(SQUARE_SIZE * 2 / 3)))
