"""
Implements the obstacles (beams of fire) hanging in the air
"""

import numpy as np
import colorama as cl
from spawnable import Spawnable


class FireBeam(Spawnable):
    """
    The FireBeam obstacles that destroy the player if colliding
    """

    def __init__(self, frame_size: tuple):
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
                frame_size[0] + 1 - 4), frame_size[1])
        elif self.type == 'Horizontal':
            self.sprite = [
                "XXXX"
            ]
            self.position = (np.random.randint(
                frame_size[0] + 1 - 1), frame_size[1])
        elif self.type == 'LeftDiagonal':
            self.sprite = [
                "X   ",
                " X  ",
                "  X ",
                "   X"
            ]
            self.position = (np.random.randint(
                frame_size[0] + 1 - 4), frame_size[1])
        elif self.type == 'RightDiagonal':
            self.sprite = [
                "   X",
                "  X ",
                " X  ",
                "X   "
            ]
            self.position = (np.random.randint(
                frame_size[0] + 1 - 4), frame_size[1])

    def __str__(self):
        return "\n".join(self.sprite)

    def update_on_timestep(self):
        """
        Move the obstacle to the right in every frame
        :return: False if it's supposed to be deleted, True otherwise
        """
        if self.delete_me:
            return
        self.position = (self.position[0], self.position[1] - 0.5)
        if self.position[0] < -4:
            self.delete_me = True

    @staticmethod
    def spawn(frame_size: tuple, prob: float = 1/50):
        to_spawn = np.random.choice([False, True], p=[1 - prob, prob])
        if to_spawn:
            return FireBeam(frame_size)
        return False
