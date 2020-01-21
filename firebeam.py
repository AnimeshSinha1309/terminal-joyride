"""
Implements the obstacles (beams of fire) hanging in the air
"""

import numpy as np
import colorama as cl
import container
from spawnable import Spawnable


class FireBeam(Spawnable):
    """
    The FireBeam obstacles that destroy the player if colliding
    """

    def __init__(self):
        self._type = np.random.choice(
            ['Vertical', 'Horizontal', 'LeftDiagonal', 'RightDiagonal'])
        self._bgcolor = cl.Back.YELLOW
        self._fgcolor = cl.Fore.BLACK
        if self._type == 'Vertical':
            self._sprite = [
                "X",
                "X",
                "X",
                "X"
            ]
            self.position = (np.random.randint(
                container.FRAME_ROWS + 1 - 4), container.FRAME_COLS)
        elif self._type == 'Horizontal':
            self._sprite = [
                "XXXX"
            ]
            self.position = (np.random.randint(
                container.FRAME_ROWS + 1 - 1), container.FRAME_COLS)
        elif self._type == 'LeftDiagonal':
            self._sprite = [
                "X   ",
                " X  ",
                "  X ",
                "   X"
            ]
            self.position = (np.random.randint(
                container.FRAME_ROWS + 1 - 4), container.FRAME_COLS)
        elif self._type == 'RightDiagonal':
            self._sprite = [
                "   X",
                "  X ",
                " X  ",
                "X   "
            ]
            self.position = (np.random.randint(
                container.FRAME_ROWS + 1 - 4), container.FRAME_COLS)

    def __str__(self):
        return "\n".join(self._sprite)

    def update_on_timestep(self):
        """
        Move the obstacle to the right in every frame
        :return: False if it's supposed to be deleted, True otherwise
        """
        if self._delete_me:
            return
        self.position = (
            self.position[0], self.position[1] - container.SCROLL_SPEED)
        if self.position[0] < -4:
            self._delete_me = True

    @staticmethod
    def spawn(prob: float = 1/50):
        to_spawn = np.random.choice([False, True], p=[1 - prob, prob])
        if to_spawn:
            return FireBeam()
        return False
