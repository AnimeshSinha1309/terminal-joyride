"""
Implement the Speed-up power-up
"""

import colorama as cl
import numpy as np
from gameobject import GameObject
import container


class PowerUp(GameObject):

    visible = False
    activated = False
    spawn_prob = 0.1
    activated_time = 0

    def update_on_timestep(self):
        if not self.visible and not self.activated:
            create = np.random.choice(
                [True, False], p=[self.spawn_prob, 1 - self.spawn_prob])
            if create:
                self.position = (np.random.randint(container.FRAME_ROWS - 1),
                                 container.FRAME_COLS)
                self.visible = True
        elif self.visible:
            self.position = (self.position[0],
                             self.position[1] - container.SCROLL_SPEED)
            if self.position[1] < 0:
                self.visible = False
        elif self.activated:
            self.activated_time -= 1
            if self.activated_time < 0:
                self.activated = False
                self.activate(False)

    def render_object(self, frame):
        if self.visible:
            super(PowerUp, self).render_object(frame)

    def respond_to_keypress(self, key):
        pass

    def activate(self, activate):
        self.visible = False
        raise NotImplementedError

    def detect_collision(self, other):
        val = (int(self.position[0]), int(
            self.position[1])) in other.get_all_coordinates()
        return val


class SpeedUp(PowerUp):

    def __init__(self):
        self.sprite = ["*"]
        self.bgcolor = cl.Back.BLUE
        self.fgcolor = cl.Fore.WHITE

    def activate(self, activate):
        if activate:
            self.visible = False
            self.activated_time = container.SPEEDUP_LIFE
            self.activated = True
            container.SCROLL_SPEED *= 2
        else:
            self.activated = False
            container.SCROLL_SPEED /= 2


class Shield(PowerUp):

    def __init__(self, player):
        self.sprite = ["+"]
        self.bgcolor = cl.Back.BLUE
        self.fgcolor = cl.Fore.WHITE
        self.player = player

    def activate(self, activate):
        if activate:
            self.visible = False
            self.activated = True
            self.activated_time = container.SHIELD_LIFE
            self.player.bgcolor = cl.Back.GREEN
            container.SHEILD_UP = True
        else:
            self.activated = False
            self.player.bgcolor = cl.Back.RED
            container.SHEILD_UP = False
