"""
The magnet that appears in the middle of the game and moves the player around.
"""

import colorama as cl
import numpy as np
import container
from gameobject import GameObject


class Magnet(GameObject):
    """
    Draws the magnet that appears once in the game
    """

    def __init__(self, player: GameObject):
        self.sprite = [
            "===",
            "| |",
            "| |"
        ]
        self.position = (np.random.randint(0, container.FRAME_ROWS),
                         np.random.randint(0, container.FRAME_COLS))
        self.fgcolor = cl.Fore.RED
        self.bgcolor = cl.Back.BLACK
        self.player = player
        self.time_elapsed = 0

    def magnet_pull(self):
        """
        Updates the position of the player, pulling him towards itself.
        """
        self.player.position = (0.8 * self.player.position[0] + 0.2 * self.position[0],
                                0.8 * self.player.position[1] + 0.2 * self.position[1])
        self.player.velocity = 0

    def update_on_timestep(self):
        """
        Call magnet pull, check if magnet time is over.
        """
        self.magnet_pull()
        self.time_elapsed += 1
        if self.time_elapsed > container.MAGNET_LIFE:
            self.delete_me = True

    def respond_to_keypress(self, key):
        return
