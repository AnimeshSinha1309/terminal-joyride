"""
The background scenery that scrolls but does not interact with anything
"""

import colorama as cl
from gameobject import GameObject


class Background(GameObject):
    """
    Class holding the basic Background, sky, ground, and scenery
    """

    def __init__(self):
        """
        Initialize the background, here does nothing
        """
        # TODO: Get dynamic frame size here, background accordingly

    def respond_to_keypress(self, key):
        """
        Implement how to respond to a random keypress
        :param key: the key that was pressed
        :return:
        """

    def update_on_timestep(self):
        """
        Implement the update functions on every timestep
        :return:
        """

    def render_object(self, frame):
        """
        Implement the way to render on the screen cache
        :param frame: the frame to print on
        :return:
        """
        frame.draw_rect((0, frame.rows), (0, frame.cols),
                        ' ', color=(cl.Back.CYAN, cl.Fore.WHITE))
        frame.draw_rect((frame.rows - 1, frame.rows), (0, frame.cols),
                        ' ', color=(cl.Back.GREEN, cl.Fore.WHITE))
