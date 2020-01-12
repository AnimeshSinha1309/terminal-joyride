"""
Implement the Boss Enemy at the end of the game.
"""

import colorama as cl
import numpy as np
from person import Person


class Boss(Person):
    """
    The FireBeam obstacles that destroy the player if colliding
    """

    def __init__(self, frame_size: tuple):
        self.bgcolor = cl.Back.BLACK
        self.fgcolor = cl.Fore.RED
        self.sprite = [
            "B",
            "O",
            "S",
            "S"
        ]
        self.position = (frame_size[0] / 2 - 3, frame_size[1])

    def update_on_timestep(self):
        """
        Move the obstacle to the right in every frame
        :return: False if it's supposed to be deleted, True otherwise
        """
        raise NotImplementedError

    @staticmethod
    def spawn(frame_size: tuple, prob: float = 1):
        """
        Spawn the Boss enemy
        :param frame_size: size of the frame to spawn in
        :param prob: probability of spawning (preferrably 1)
        """
        to_spawn = np.random.choice([False, True], p=[1 - prob, prob])
        if to_spawn:
            return Boss(frame_size)
        return False
