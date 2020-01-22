"""
Provides the Player class which keeps track of the position and renders
the player object.
"""

import colorama as cl
from person import Person
from frame import Frame
from bullets import MyBullet
import container


class Player(Person):
    """
    Stores the Player class with the following major properties:
    :property Score: int, score of the player
    :property Position: (row, col) index of the top left corner of sprite
    :property _velocity: int, _velocity
    """

    _position = (20, 4)
    _sprite = [
        " O ",
        "/|\\",
        "/ \\"
    ]
    _bgcolor = cl.Back.RED
    _fgcolor = cl.Fore.WHITE
    _bullets = []

    def __init__(self):
        self._velocity = 0
        self.last_died = -1000
        self.__inactive_sprite = False

    def __str__(self):
        return "\n".join(self._sprite)

    def render_object(self, frame: Frame):
        """
        Implement the way to render on the screen cache
        :param frame: the frame to print on
        :return:
        """
        if self._delete_me or self.__inactive_sprite:
            return
        frame.draw_sprite((int(self._position[0]), int(self._position[1])),
                          self._sprite, ' ', (self._bgcolor, self._fgcolor))
        for bullet in self._bullets:
            bullet.render_object(frame)

    def respond_to_keypress(self, key):
        """
        Implement how to respond to a random keypress
        :param key: the key that was pressed
        :return:
        """
        if self._delete_me or self.__inactive_sprite:
            return
        if key == 'a':
            self._position = (self._position[0], max(self._position[1] - 1, 2))
        elif key == 'd':
            self._position = (self._position[0], min(
                self._position[1] + 1, 60))
        elif key == 'w':
            self._position = (max(self._position[0] - 3, 1), self._position[1])
        elif key == 'f':
            self._bullets.append(MyBullet(self._position))

    def shoot_bullet(self):
        self._bullets.append(MyBullet(self._position))

    def update_on_timestep(self):
        """
        Implement the update functions on every timestep
        :return:
        """
        if self._delete_me:
            return
        self._velocity += container.SCROLL_SPEED * 0.2
        y_coord = min(self._position[0] + self._velocity, 20)
        if y_coord >= 19.7:
            self._velocity = 0
        self._position = (y_coord, self._position[1])
        for bullet in self._bullets:
            bullet.update_on_timestep()

    @property
    def bgcolor(self):
        """
        Defines the Background color property of the player
        """
        return self._bgcolor

    @bgcolor.setter
    def bgcolor(self, new_color):
        self._bgcolor = new_color

    @property
    def velocity(self):
        """
        Defines the Velocity property of the player
        """
        return self._velocity

    @velocity.setter
    def velocity(self, new_velocity):
        self._velocity = new_velocity

    def delete_sprite(self, delete):
        """
        Delete this sprite as Drogon is present
        """
        if delete:
            self.__inactive_sprite = True
        else:
            self.__inactive_sprite = False


if __name__ == '__main__':
    PLAYER = Player()
    print(PLAYER)
    print(PLAYER.get_all_coordinates())
