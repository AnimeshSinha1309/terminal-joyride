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

    activated = False
    refill_time = 0
    usable_time = 0

    def update_on_timestep(self):
        if self.activated:
            if self.usable_time > 0:
                self.usable_time -= 1
            else:
                self.activated = False
                self.activate(False)
                self.refill_time = container.SHIELD_REFILL
        elif not self.activated:
            if self.refill_time > 0:
                self.refill_time -= 1

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
            self.activated = True
            self.usable_time = container.SPEEDUP_LIFE
            container.SCROLL_SPEED *= 5
        else:
            self.activated = False
            container.SCROLL_SPEED /= 5

    def respond_to_keypress(self, key):
        if key == 'v' and self.refill_time == 0 and not self.activated:
            self.activate(True)


class Shield(PowerUp):
    """
    Implements the Shield PowerUp
    """

    def __init__(self, player):
        self.player = player

    def activate(self, activate):
        if activate:
            self.activated = True
            self.player.bgcolor = cl.Back.GREEN
            self.usable_time = container.SHIELD_LIFE
            container.SHEILD_UP = True
        else:
            self.activated = False
            self.player.bgcolor = cl.Back.RED
            container.SHEILD_UP = False

    def respond_to_keypress(self, key):
        if key == ' ' and self.refill_time == 0 and not self.activated:
            self.activate(True)
