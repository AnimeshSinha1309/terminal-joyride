"""
Implement our friendly Dragon
"""

import math
import numpy as np
import colorama as cl
from gameobject import GameObject


class Drogon(GameObject):
    """
    Implements the wavy dragon, just the display part
    """

    @staticmethod
    def _draw_wave(img, thickness=2, offset=0, char='0', till=100):
        assert(isinstance(img, np.ndarray) and len(img.shape) == 2)
        height, width = img.shape[0] - thickness, min(img.shape[1], till)
        wavelength = 20

        def start_fn(x_coord):
            return int(
                height * (math.sin(2 * math.pi * (x_coord + offset) / wavelength) + 1) / 2)
        for i in range(width):
            start = start_fn(i)
            for j in range(thickness):
                img[j + start][i] = char
        last = start_fn(width) + thickness / 2
        return (round(last), round(width))

    @staticmethod
    def _draw_head(img, center_y, start_x, height, char):
        for i in range(height):
            for j in range(int(center_y - (height - i) + 1), int(center_y + (height - i))):
                if j < 0 or j >= img.shape[0]:
                    continue
                img[j][start_x + i] = char

    def draw_img(self, height, width, offset, head_size=2):
        """
        Draws the sprite for Drogon
        """
        img = np.array([[' ' for _ in range(width)] for _ in range(height)])
        coord = self._draw_wave(img, offset=offset, till=width-head_size)
        self._draw_head(img, coord[0], coord[1], head_size, '>')
        return img

    def __init__(self):
        self.position = (4, -30)
        self._offset = 0
        self._bgcolor = cl.Back.RED
        self._fgcolor = cl.Fore.WHITE

    def render_object(self, frame):
        if not self._delete_me:
            img = self.draw_img(6, 30, int(self._offset))
            _sprite = ["".join(line) for line in img]
            frame.draw_sprite(self.position, _sprite,
                              color=(self._bgcolor, self._fgcolor))

    def update_on_timestep(self):
        self._offset += 0.1
        self.position = (self.position[0], min(self.position[1] + 1, 10))

    def respond_to_keypress(self, key):
        pass


if __name__ == "__main__":
    import time
    import osmanager

    DROGON = Drogon()
    SPRITE = DROGON.draw_img(5, 40, 0)
    for row in SPRITE:
        for col in row:
            print(col, end='')
        print()
    input()

    for c in range(1000):
        SPRITE = DROGON.draw_img(5, 40, c)
        for row in SPRITE:
            for col in row:
                print(col, end='')
            print()
        time.sleep(0.1)
        osmanager.clrscr()
