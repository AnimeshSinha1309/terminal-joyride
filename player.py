"""
Provides the Player class which keeps track of the position and renders
the player object.
"""

import colorama as cl
from person import Person
from frame import Frame
from bullets import MyBullet


class Player(Person):
    """
    Stores the Player class with the following major properties:
    :property Lives: int, lives left with the player
    :property Score: int, score of the player
    :property Position: (row, col) index of the top left corner of sprite
    :property Velocity: int, velocity
    """

    def __init__(self):
        self.position = (20, 4)
        self.sprite = [
            " O ",
            "/|\\",
            "/ \\"
        ]
        self.bgcolor = cl.Back.RED
        self.fgcolor = cl.Fore.WHITE
        self.last_died = -10000
        self.bullets = []

    def __str__(self):
        return "\n".join(self.sprite)

    def render_object(self, frame: Frame):
        """
        Implement the way to render on the screen cache
        :param frame: the frame to print on
        :return:
        """
        if self.delete_me:
            return
        frame.draw_sprite((int(self.position[0]), int(self.position[1])),
                          self.sprite, ' ', (self.bgcolor, self.fgcolor))
        for bullet in self.bullets:
            bullet.render_object(frame)

    def respond_to_keypress(self, key):
        """
        Implement how to respond to a random keypress
        :param key: the key that was pressed
        :return:
        """
        if self.delete_me:
            return
        if key == 'a':
            self.position = (self.position[0], max(self.position[1] - 1, 2))
        elif key == 'd':
            self.position = (self.position[0], min(self.position[1] + 1, 60))
        elif key == 'w':
            self.position = (max(self.position[0] - 3, 1), self.position[1])
        elif key == 'f':
            self.bullets.append(MyBullet(self.position))

    def shoot_bullet(self):
        self.bullets.append(MyBullet(self.position))

    def update_on_timestep(self):
        """
        Implement the update functions on every timestep
        :return:
        """
        if self.delete_me:
            return
        y_coord = min(self.position[0] + 1, 20)
        self.position = (y_coord, self.position[1])
        for bullet in self.bullets:
            bullet.update_on_timestep()


if __name__ == '__main__':
    PLAYER = Player()
    print(PLAYER)
    print(PLAYER.get_all_coordinates())
