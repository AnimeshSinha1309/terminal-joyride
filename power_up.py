"""
Implement the Speed-up power-up
"""

import colorama as cl
from gameobject import GameObject
import container


class PowerUp(GameObject):
    """
    General Updates and Attributes of each power-up
    Does not get rendered, just accepts keygrabs
    """

    _activated = False
    _refill_time = 0
    _usable_time = 0

    def update_on_timestep(self):
        if self._activated:
            if self._usable_time > 0:
                self._usable_time -= 1
            else:
                self._activated = False
                self.activate(False)
                self._refill_time = container.SHIELD_REFILL
        elif not self._activated:
            if self._refill_time > 0:
                self._refill_time -= 1

    def render_object(self, frame):
        pass

    def respond_to_keypress(self, key):
        """
        Press the button to activate the shield
        """
        raise NotImplementedError

    def activate(self, activate):
        """
        Call this to activate or deactivate the power-up affecting the other
        actors in the game
        :param activate: boolean, True if activate, False if deactivate
        """
        raise NotImplementedError

    def detect_collision(self, other):
        return False


class SpeedUp(PowerUp):
    """
    Implements the SpeedUp PowerUp
    """

    def __init__(self):
        pass

    def activate(self, activate):
        if activate:
            self._activated = True
            self._usable_time = container.SPEEDUP_LIFE
            container.SCROLL_SPEED *= 5
        else:
            self._activated = False
            container.SCROLL_SPEED /= 5

    def respond_to_keypress(self, key):
        if key == 'v' and self._refill_time == 0 and not self._activated:
            self.activate(True)


class Shield(PowerUp):
    """
    Implements the Shield PowerUp
    """

    def __init__(self, player):
        self.player = player

    def activate(self, activate):
        if activate:
            self._activated = True
            self.player.bgcolor = cl.Back.GREEN
            self._usable_time = container.SHIELD_LIFE
            container.SHEILD_UP = True
        else:
            self._activated = False
            self.player.bgcolor = cl.Back.RED
            container.SHEILD_UP = False

    def respond_to_keypress(self, key):
        if key == ' ' and self._refill_time == 0 and not self._activated:
            self.activate(True)
