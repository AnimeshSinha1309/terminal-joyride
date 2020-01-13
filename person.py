"""
Stores the Person class which holds common properties
of all active mobile objects.
"""

from gameobject import GameObject


class Person(GameObject):
    """
    Implements the Person class to be inherited
    by Player and Enemy Boss
    """

    def render_object(self, frame):
        raise NotImplementedError

    def update_on_timestep(self):
        raise NotImplementedError

    def respond_to_keypress(self, key):
        raise NotImplementedError

    def shoot_bullet(self):
        raise NotImplementedError
