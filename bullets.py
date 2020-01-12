"""
Contains classes for both my Bullets and the enemy Bullets
"""

import colorama as cl
from gameobject import GameObject
import container


class MyBullet(GameObject):

    def __init__(self, position):
        self.sprite = ["=>"]
        self.bgcolor = cl.Back.WHITE
        self.fgcolor = cl.Fore.RED
        self.position = (position[0] + 1, position[1] + 3)

    def update_on_timestep(self):
        self.position = (self.position[0], self.position[1] + 2)
        if self.position[1] > container.FRAME_COLS:
            self.delete_me = True

    def render_object(self, frame):
        return super().render_object(frame)

    def respond_to_keypress(self, key):
        return


class EnemyBullet(GameObject):

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

    def render_object(self, frame):
        return super().render_object(frame)

    def respond_to_keypress(self, key):
        return
