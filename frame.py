import colorama
import numpy as np
import os
import osmanager
import colorama as cl
import time


class Frame:

    def __init__(self):
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
        for row in range(self.ROWS):
            for col in range(self.COLS):
                print(self.bgcolor[row][col] + self.fgcolor[row]
                      [col] + self.text[row][col], end='')
            print(cl.Style.RESET_ALL)
        self.previous_render_time = time.time()

    def draw_rect(self, top, bot, left, right,
                  char='.', bgcolor=cl.Back.CYAN, fgcolor=cl.Fore.WHITE):
        for i in range(top, bot):
            for j in range(left, right):
                self.text[i][j] = char
                self.bgcolor[i][j] = bgcolor
                self.fgcolor[i][j] = fgcolor

    def draw_ellipse(self, center_row, center_col, row_radius, col_radius,
                     char='.', bgcolor=cl.Back.BLACK, fgcolor=cl.Fore.WHITE):
        for i in range(center_row - row_radius, center_row + row_radius):
            for j in range(center_col - col_radius, center_col + col_radius):
                if ((center_row - i) / row_radius) ** 2 + ((center_col - j) / col_radius) ** 2 <= 1:
                    self.text[i][j] = char
                    self.bgcolor[i][j] = bgcolor
                    self.fgcolor[i][j] = fgcolor

    def broadcast_input(self):
        ch = osmanager.getch()
        if ch == -1:
            return


if __name__ == '__main__':
    x = Frame()
    x.draw_ellipse(13, 50, 5, 10, bgcolor=cl.Back.MAGENTA)
    x.draw_rect(3, 5, 10, 20, bgcolor=cl.Back.MAGENTA, fgcolor=cl.Fore.BLACK)
    FRAME_RATE = 10
    while True:
        if time.time() > x.previous_render_time + 1 / FRAME_RATE:
            x.broadcast_input()
            osmanager.clrscr()
            x.render()
