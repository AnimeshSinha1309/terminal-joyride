"""
Keeps the central frame rendering class.
"""

import time
import numpy as np
import colorama as cl
import osmanager
import container


class Frame:
    """
    Stores the Frame class with the following major attributes:
    :property _text: image matrix - text part
    :property _bgcolor: image matrix - background color part
    :property _fgcolor: image matrix - foreground color part
    :property _previous_render_time: last refresh time
    """

    def __init__(self):
        """
        Initialize the rendering frame
        """
        osmanager.hide_cursor()
        self._text = np.array(
            [np.array([' ' for _ in range(container.FRAME_COLS)])
             for _ in range(container.FRAME_ROWS)])
        self._bgcolor = np.array(
            [np.array([cl.Back.CYAN for _ in range(container.FRAME_COLS)])
             for _ in range(container.FRAME_ROWS)])
        self._fgcolor = np.array(
            [np.array([cl.Fore.WHITE for _ in range(container.FRAME_COLS)])
             for _ in range(container.FRAME_ROWS)])
        self._previous_render_time = time.time()

    def render(self):
        """
        Renders the cached array onto the terminal
        """
        for row in range(container.FRAME_ROWS):
            for col in range(container.FRAME_COLS):
                print(self._bgcolor[row][col] + self._fgcolor[row]
                      [col] + self._text[row][col], end='')
            print(cl.Style.RESET_ALL)
        self._previous_render_time = time.time()

        print("Score: {0:4} {3} Lives: {1:2} {3} Time Remaining: {2:4}"
              .format(container.SCORE, container.LIVES, container.TIME_REMAINING // 10, ' ' * 18),
              end='', flush=True)

    def draw_rect(self, row_limits: tuple, col_limits: tuple,
                  char='.', color: tuple = (cl.Back.CYAN, cl.Fore.WHITE)):
        """
        Draws a rectangle on the game frame
        :param row_limits: starting and ending row (top-inclusive, bottom-exclusive)
        :param col_limits: starting and ending col (left-inclusive, right-exclusive)
        :param char: the character used to print the figure
        :param color: pair of (background, foreground) color
        """
        for i in range(row_limits[0], row_limits[1]):
            for j in range(col_limits[0], col_limits[1]):
                if not self.in_frame_bounds(i, j):
                    continue
                self._text[i][j] = char
                self._bgcolor[i][j] = color[0]
                self._fgcolor[i][j] = color[1]

    def draw_ellipse(self, center: tuple, radius: tuple,
                     char='.', color: tuple = (cl.Back.BLACK, cl.Fore.WHITE)):
        """
        Draws an ellipse on the game frame
        :param center: (x, y) of the center of ellipse
        :param radius: semi-major and semi-minor axis (row, col)
        :param char: the character used to print the figure
        :param color: colorama.Fore, Color of the Background for the sprite
        """
        for i in range(center[0] - radius[0], center[0] + radius[0]):
            for j in range(center[1] - radius[1], center[1] + radius[1]):
                if not self.in_frame_bounds(i, j):
                    continue
                if ((center[0] - i) / radius[0]) ** 2 + ((center[1] - j) / radius[1]) ** 2 <= 1:
                    self._text[i][j] = char
                    self._bgcolor[i][j] = color[0]
                    self._fgcolor[i][j] = color[1]

    def draw_sprite(self, _position: tuple, image: list, skip_char: str = ' ',
                    color: tuple = (cl.Back.BLACK, cl.Fore.WHITE)):
        """
        Draws the sprite on the game frame which is passed in as an array of strings
        :param _position: pair of (row _position, col _position) for the top-left corner
        :param image: array of strings that represent the image to be drawn
        :param skip_char: char, the character that is not a part of the sprite, so don't color it
        :param color: pair of Background color and Foreground color
        """
        assert not image or isinstance(image[0], str)
        assert len(_position) == 2 and len(skip_char) == 1
        for i, _ in enumerate(image):
            for j, cell in enumerate(image[i]):
                if not self.in_frame_bounds(i, j) or \
                        not self.in_frame_bounds(i + _position[0], j + _position[1]):
                    continue
                if image[i][j] != skip_char:
                    self._text[i + _position[0]][j + _position[1]] = cell
                    if color[0] != "":
                        self._bgcolor[i + _position[0]
                                      ][j + _position[1]] = color[0]
                    if color[1] != "":
                        self._fgcolor[i + _position[0]
                                      ][j + _position[1]] = color[1]

    @staticmethod
    def broadcast_input(objects):
        """
        Broadcasts the received input to all the objects
        :param objects: objects to broadcast to
        :return:
        """
        character = osmanager.getch()
        if character == -1:
            return
        if character == 'q':
            osmanager.sys_exit()
        for item in objects:
            if not item.delete_me:
                item.respond_to_keypress(character)

    def broadcast_render(self, objects):
        """
        Broadcasts the rendering step to all the objects
        :param objects: objects to be rendered
        :return:
        """
        for item in objects:
            if not item.delete_me:
                item.render_object(self)

    @staticmethod
    def broadcast_timestep(objects):
        """
        Broadcasts the timestep event to all the objects
        :param objects: objects to be updated
        :return:
        """
        for item in objects:
            if not item.delete_me:
                item.update_on_timestep()

    @staticmethod
    def in_frame_bounds(i: int, j: int):
        """
        Check if (i, j) is in frame
        :param i: row index
        :param j: col index
        :return: True if it is in, False otherwise
        """
        return 0 <= i < container.FRAME_ROWS and 0 <= j < container.FRAME_COLS

    @staticmethod
    def player_die():
        """
        Reduces the lives and moves to the exit sequence if lives = 0
        """
        container.LIVES -= 1
        if container.LIVES <= 0:
            container.exit_sequence(False)

    @property
    def previous_render_time(self):
        """
        Defines as a property the last time the frame was rendered to set the frame rate.
        """
        return self._previous_render_time

    @previous_render_time.setter
    def previous_render_time(self, new_value):
        self._previous_render_time = new_value


if __name__ == '__main__':
    X = Frame()
    X.draw_ellipse((13, 50), (5, 10), color=(cl.Back.MAGENTA, cl.Fore.WHITE))
    X.draw_rect((3, 5), (10, 20), color=(cl.Back.MAGENTA, cl.Fore.BLACK))
    FRAME_RATE = 10
    while True:
        if time.time() > X.previous_render_time + 1 / FRAME_RATE:
            X.broadcast_input([])
            osmanager.clrscr()
            X.render()
