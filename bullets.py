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

    def __init__(self, _position):
        self._sprite = ["=>"]
        self._bgcolor = cl.Back.WHITE
        self._fgcolor = cl.Fore.RED
        self._position = (_position[0] + 1, _position[1] + 3)

    def update_on_timestep(self):
        self._position = (
            self._position[0], self._position[1] + container.SCROLL_SPEED * 4)
        if self._position[1] > container.FRAME_COLS:
            self._delete_me = True

    def respond_to_keypress(self, key):
        return

    def detect_collision(self, other):
        for point in other.get_all_coordinates():
            if 0 <= int(self._position[0]) - int(point[0]) < 1 and \
                    -3 <= int(self._position[1]) - int(point[1]) < 2:
                return True
        return False


class EnemyBullet(GameObject):
    """
    The bullets class, parameters hardcoded for the boss bullets
    """

    def __init__(self, _position):
        self._sprite = [
            "/==",
            "\\=="
        ]
        self._bgcolor = cl.Back.WHITE
        self._fgcolor = cl.Fore.RED
        self._position = (_position[0] + 5, _position[1] - 3)

    def update_on_timestep(self):
        self._position = (
            self._position[0], self._position[1] - container.SCROLL_SPEED * 8)
        if self._position[1] < 0:
            self._delete_me = True

    def respond_to_keypress(self, key):
        return

    def detect_collision(self, other):
        for point in other.get_all_coordinates():
            if 0 <= int(point[0]) - int(self._position[0]) < 3 and \
                    0 <= int(point[1]) - int(self._position[1]) < 2:
                return True
        return False
