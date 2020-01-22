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

    _bullets = []

    def render_object(self, frame):
        raise NotImplementedError

    def update_on_timestep(self):
        raise NotImplementedError

    def respond_to_keypress(self, key):
        raise NotImplementedError

    def shoot_bullet(self):
        """
        Functional interface to shoot bullets out
        """
        raise NotImplementedError

    @property
    def bullets(self):
        """
        Returns the list of bullets that the person has shot
        """
        return self._bullets
