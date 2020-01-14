"""
Implement the Speed-up power-up
"""

import colorama as cl
import numpy as np
from gameobject import GameObject
import container


class PowerUp(GameObject):

    visible = False
    spawn_prob = 0.1

    def update_on_timestep(self):
        if not self.visible:
            create = np.random.choice([True, False], p=[self.spawn_prob, 1 - self.spawn_prob])
            if create:
                self.position = (np.random.randint(container.FRAME_ROWS - 1),
                                 container.FRAME_COLS)
                self.activate(True)
                self.visible = True
        else:
            self.position = (self.position[0],
                             self.position[1] - container.SCROLL_SPEED)
            if self.position[1] < 0:
                self.visible = False
                self.activate(False)

    def respond_to_keypress(self, key):
        pass

    def activate(self, do):
        raise NotImplementedError


class SpeedUp(PowerUp):

    def __init__(self):
        self.sprite = ["*"]
        self.bgcolor = cl.Back.BLUE
        self.fgcolor = cl.Fore.WHITE

    def activate(self, do):
        if do:
            pass
        else:
            pass


class Shield(PowerUp):

    def __init__(self):
        self.sprite = ["+"]
        self.bgcolor = cl.Back.BLUE
        self.fgcolor = cl.Fore.WHITE

    def activate(self, do):
        if do:
            pass
        else:
            pass
