import numpy as np
from .config import ROWS, COLUMNS, NUM_MOVES


class QLearning:
    def __init__(self, gamma, alpha):
        self.gamma = gamma
        self.alpha = alpha
        self.q_table = np.zeros((ROWS, COLUMNS, NUM_MOVES))

    def select_action(self, state):
        action = np.argmax(self.q_table[state])
        return action

    def optimize(self, state, action, next_state, reward):
        old_value = self.q_table[state[0], state[1], action]
        next_max = np.max(self.q_table[next_state])

        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)
        self.q_table[state[0], state[1], action] = new_value
        print("Q_table optimized")


