"""
Contains classes for both my Bullets and the enemy Bullets
"""

import colorama as cl
from gameobject import GameObject
import container


class MyBullet(GameObject):
    """
    The bullets class, parameters hardcoded for the myre bullets
    """

    def __init__(self, position):
        self.sprite = ["=>"]
        self.bgcolor = cl.Back.WHITE
        self.fgcolor = cl.Fore.RED
        self.position = (position[0] + 1, position[1] + 3)

    def update_on_timestep(self):
        self.position = (self.position[0], self.position[1] + 2)
        if self.position[1] > container.FRAME_COLS:
            self.delete_me = True

    def respond_to_keypress(self, key):
        return

    def detect_collision(self, other):
        for point in other.get_all_coordinates():
            if 0 <= int(self.position[0]) - int(point[0]) < 2 and \
                    0 <= int(self.position[1]) - int(point[1]) < 1:
                return True
        return False


class EnemyBullet(GameObject):
    """
    The bullets class, parameters hardcoded for the boss bullets
    """

    def __init__(self, position):
        self.sprite = [
            "/==",
            "\\=="
        ]
        self.bgcolor = cl.Back.WHITE
        self.fgcolor = cl.Fore.RED
        self.position = (position[0] + 5, position[1] - 3)

    def update_on_timestep(self):
        self.position = (self.position[0], self.position[1] - 4)
        if self.position[1] < 0:
            self.delete_me = True

    def respond_to_keypress(self, key):
        return

    def detect_collision(self, other):
        for point in other.get_all_coordinates():
            if 0 <= int(point[0]) - int(self.position[0]) < 3 and \
                    0 <= int(point[1]) - int(self.position[1]) < 2:
                return True
        return False
