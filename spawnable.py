"""
Contains Abstract class for all spawnable objects
"""

from gameobject import GameObject


class Spawnable(GameObject):
    """
    Obstacles that are spawnable are random positions,
    Fire Beams, Magnets, Bullets, Power-Ups, Boss, etc.
    """

    def update_on_timestep(self):
        """
        Update on the next timestep the state of the object
        """
        raise NotImplementedError

    def respond_to_keypress(self, key):
        """
        Repond the the keypress broadcasted by the frame
        :param key: the key that was pressed
        """

    @staticmethod
    def spawn(frame_size: tuple, prob: float):
        """
        Randomly decides whether or not to spawn an object here
        :param frame_size: (rows, cols) in the frame
        :param prob: the probability for spawning
        """
        raise NotImplementedError
