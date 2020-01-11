"""
Has the fundamental Abstract class for all objects in the game.
"""

from abc import ABC


class GameObject(ABC):
    """
    Abstract Class describing the features that every object
    in the game must bear.

    The following methods must be implemented:
    * __init__()
    * __str__()
    * respond_to_keypress(key)
    * update_on_timestep()
    * render_object(frame)
    """

    def respond_to_keypress(self, key):
        """
        Implement how to respond to a random keypress
        :param key: the key that was pressed
        :return:
        """
        raise NotImplementedError

    def update_on_timestep(self):
        """
        Implement the update functions on every timestep
        :return:
        """
        raise NotImplementedError

    def render_object(self, frame):
        """
        Implement the way to render on the screen cache
        :param frame: the frame to print on
        :return:
        """
        raise NotImplementedError
