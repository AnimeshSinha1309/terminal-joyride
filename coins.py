"""
Creates random coins in the sky that add to your score, Yay!
"""

import numpy as np
import colorama as cl
from spawnable import Spawnable
import container


class Coin(Spawnable):
    """
    Random coins for scoring points
    """

    def __init__(self, position: tuple):
        self.sprite = ["$"]
        self.fgcolor = cl.Fore.YELLOW
        self.bgcolor = cl.Back.BLACK
        self.position = position

    @staticmethod
    def spawn(prob: float = 1/500):
        create = np.random.choice([True, False], p=[prob, 1 - prob])
        if not create:
            return []
        size = (np.random.randint(2, 5), np.random.randint(2, 7))
        selected_row = np.random.randint(container.FRAME_ROWS - size[0])
        return [Coin((row + selected_row, col + container.FRAME_COLS))
                for row in range(0, size[0] - 1)
                for col in range(0, size[1] - 1)]

    def update_on_timestep(self):
        self.position = (
            self.position[0], self.position[1] - container.SCROLL_SPEED)

    def detect_collision(self, other):
        return self.position in other.get_all_coordinates()
