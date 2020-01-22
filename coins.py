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

    def __init__(self, _position: tuple):
        self._sprite = ["$"]
        self._fgcolor = cl.Fore.YELLOW
        self._bgcolor = ""
        self._position = _position

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
        self._position = (
            self._position[0], self._position[1] - container.SCROLL_SPEED)

    def detect_collision(self, other):
        val = (int(self._position[0]), int(
            self._position[1])) in other.get_all_coordinates()
        return val
