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
        self.type = np.random.choice(
            ['Vertical', 'Horizontal', 'LeftDiagonal', 'RightDiagonal'])
        self.bgcolor = cl.Back.YELLOW
        self.fgcolor = cl.Fore.BLACK
        if self.type == 'Vertical':
            self.sprite = [
                "X",
                "X",
                "X",
                "X"
            ]
            self.position = (np.random.randint(
                container.FRAME_ROWS + 1 - 4), container.FRAME_COLS)
        elif self.type == 'Horizontal':
            self.sprite = [
                "XXXX"
            ]
            self.position = (np.random.randint(
                container.FRAME_ROWS + 1 - 1), container.FRAME_COLS)
        elif self.type == 'LeftDiagonal':
            self.sprite = [
                "X   ",
                " X  ",
                "  X ",
                "   X"
            ]
            self.position = (np.random.randint(
                container.FRAME_ROWS + 1 - 4), container.FRAME_COLS)
        elif self.type == 'RightDiagonal':
            self.sprite = [
                "   X",
                "  X ",
                " X  ",
                "X   "
            ]
            self.position = (np.random.randint(
                container.FRAME_ROWS + 1 - 4), container.FRAME_COLS)

    def __str__(self):
        return "\n".join(self.sprite)

    def update_on_timestep(self):
        """
        Move the obstacle to the right in every frame
        :return: False if it's supposed to be deleted, True otherwise
        """
        if self.delete_me:
            return
        self.position = (
            self.position[0], self.position[1] - container.SCROLL_SPEED)
        if self.position[0] < -4:
            self.delete_me = True

    @staticmethod
    def spawn(prob: float = 1/50):
        to_spawn = np.random.choice([False, True], p=[1 - prob, prob])
        if to_spawn:
            return FireBeam()
        return False
