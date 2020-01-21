"""
Has the fundamental Abstract class for all objects in the game.
"""

from abc import ABC
import colorama as cl


class GameObject(ABC):
    """
    Abstract Class describing the features that every object
    in the game must bear.

    The following methods must be implemented:
    * __str__()
    * respond_to_keypress(key)
    * update_on_timestep()
    * render_object(frame)
    """

    _sprite = ""
    position = (0, 0)
    _bgcolor = cl.Back.BLACK
    _fgcolor = cl.Fore.WHITE
    _delete_me = False

    def __str__(self):
        return "\n".join(self._sprite)

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

    def get_all_coordinates(self):
        """
        Returns all coordinates where the firebeam is present (can collide)
        :return: list of tuples (i, j), coordinates where the firebeam is present
        """
        return [(int(i + self.position[0]), int(j + self.position[1]))
                for i, row in enumerate(self._sprite)
                for j, cell in enumerate(row)
                if cell != ' ']

    def detect_collision(self, other):
        """
        Check if there is a collision with another object
        :param other: object with which to check
        :return: True if colliding, False otherwise
        """
        coords = self.get_all_coordinates() + other.get_all_coordinates()
        return len(set(coords)) < len(coords)

    def render_object(self, frame):
        """
        Implement the way to render on the screen cache
        :param frame: the frame to print on
        :return:
        """
        if not self._delete_me:
            frame.draw_sprite((int(self.position[0]), int(self.position[1])),
                              self._sprite, ' ', (self._bgcolor, self._fgcolor))

    @property
    def delete_me(self):
        """
        Property that marks the object for deletion
        """
        return self._delete_me

    @delete_me.setter
    def delete_me(self, new_value):
        self._delete_me = new_value
