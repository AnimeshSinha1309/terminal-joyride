import colorama
import numpy as np
import os
import osmanager
import colorama as cl
import time
from gameobject import GameObject


class Frame:

    def __init__(self):
        """
        Initialize the rendering frame
        """
        osmanager.hide_cursor()
        self.ROWS = 24
        self.COLS = 80
        self.text = np.array(
            [np.array([' ' for _ in range(self.COLS)]) for _ in range(self.ROWS)])
        self.bgcolor = np.array(
            [np.array([cl.Back.CYAN for _ in range(self.COLS)]) for _ in range(self.ROWS)])
        self.fgcolor = np.array(
            [np.array([cl.Fore.WHITE for _ in range(self.COLS)]) for _ in range(self.ROWS)])
        self.previous_render_time = time.time()

    def render(self):
        """
        Renders the cached array onto the terminal
        """
        for row in range(self.ROWS):
            for col in range(self.COLS):
                print(self.bgcolor[row][col] + self.fgcolor[row]
                      [col] + self.text[row][col], end='')
            print(cl.Style.RESET_ALL)
        self.previous_render_time = time.time()

    def draw_rect(self, top, bot, left, right,
                  char='.', bgcolor=cl.Back.CYAN, fgcolor=cl.Fore.WHITE):
        """
        Draws a rectangle on the game frame

        Parameters
        ==========
        top: row index of the center [inclusive]
        bot: column index of the center [exclusive]
        left: radius along the row index (one of the semi-axis of ellipse) [inclusive]
        right: radius along the col index (one of the semi-axis of ellipse) [exclusive]
        char: the character used to print the figure
        bgcolor: colorama.Fore, Color of the Background for the sprite
        fgcolor: colorama.Back, Color of the Foreground for the sprite
        """
        for i in range(top, bot):
            for j in range(left, right):
                if not self.in_frame_bounds(i, j):
                    continue
                self.text[i][j] = char
                self.bgcolor[i][j] = bgcolor
                self.fgcolor[i][j] = fgcolor

    def draw_ellipse(self, center_row, center_col, row_radius, col_radius,
                     char='.', bgcolor=cl.Back.BLACK, fgcolor=cl.Fore.WHITE):
        """
        Draws an ellipse on the game frame

        Parameters
        ==========
        center_row: row index of the center
        center_col: column index of the center
        row_radius: radius along the row index (one of the semi-axis of ellipse)
        col_radius: radius along the col index (one of the semi-axis of ellipse)
        char: the character used to print the figure
        bgcolor: colorama.Fore, Color of the Background for the sprite
        fgcolor: colorama.Back, Color of the Foreground for the sprite
        """
        for i in range(center_row - row_radius, center_row + row_radius):
            for j in range(center_col - col_radius, center_col + col_radius):
                if not self.in_frame_bounds(i, j):
                    continue
                if ((center_row - i) / row_radius) ** 2 + ((center_col - j) / col_radius) ** 2 <= 1:
                    self.text[i][j] = char
                    self.bgcolor[i][j] = bgcolor
                    self.fgcolor[i][j] = fgcolor

    def draw_sprite(self, position: tuple, image: list, skip_char: str = ' ',
                    bgcolor=cl.Back.BLACK, fgcolor=cl.Fore.WHITE):
        """
        Draws the sprite on the game frame which is passed in as an array of strings

        Parameters
        ==========
        position: pair of (row position, col position) for the top-left corner
        image: array of strings that represent the image to be drawn
        skip_char: char, the character that is not a part of the sprite, so don't color it
        bgcolor: colorama.Fore, Color of the Background for the sprite
        fgcolor: colorama.Back, Color of the Foreground for the sprite
        """
        assert len(image) == 0 or type(image[0]) is str
        assert len(position) == 2 and len(skip_char) == 1
        for i in range(len(image)):
            for j in range(len(image[i])):
                if not self.in_frame_bounds(i, j) or not self.in_frame_bounds(i + position[0], j + position[1]):
                    continue
                self.text[i + position[0]][j + position[1]] = image[i][j]
                if image[i][j] != skip_char:
                    self.bgcolor[i + position[0]][j + position[1]] = bgcolor
                    self.fgcolor[i + position[0]][j + position[1]] = fgcolor

    def broadcast_input(self, objects):
        ch = osmanager.getch()
        if ch == -1:
            return
        if ch == 'q':
            osmanager.sys_exit()
        for item in objects:
            item.respond_to_keypress(ch)

    def broadcast_render(self, objects):
        for item in objects:
            item.render_object(self)

    def broadcase_timestep(self, objects):
        for item in objects:
            item.update_on_timestep()

    def in_frame_bounds(self, i: int, j: int):
        return i >= 0 and i < self.ROWS and j >= 0 and j < self.COLS


if __name__ == '__main__':
    x = Frame()
    x.draw_ellipse(13, 50, 5, 10, bgcolor=cl.Back.MAGENTA)
    x.draw_rect(3, 5, 10, 20, bgcolor=cl.Back.MAGENTA, fgcolor=cl.Fore.BLACK)
    FRAME_RATE = 10
    while True:
        if time.time() > x.previous_render_time + 1 / FRAME_RATE:
            x.broadcast_input([])
            osmanager.clrscr()
            x.render()
