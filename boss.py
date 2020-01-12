"""
Implement the Boss Enemy at the end of the game.
"""

import colorama as cl
from person import Person
from player import Player


class Boss(Person):
    """
    The FireBeam obstacles that destroy the player if colliding
    """

    def __init__(self, frame_size: tuple, player: Player):
        self.bgcolor = cl.Back.BLACK
        self.fgcolor = cl.Fore.RED
        self.sprite = [
            "&&&&.----.__ &",
            "&&&/---.__  \\&",
            "&&/       `\\ |",
            "&| o     o  \\|",
            "/| .vvvvv.  |\\",
            "/| |     |  |\\",
            "&| `^vvvv'  |&",
            "&\\__________|&"
        ]
        self.position = (int(frame_size[0] / 2 - 3), frame_size[1])
        self.player = player
        self.frame_size = frame_size

    def render_object(self, frame):
        """
        Implement the way to render on the screen cache
        :param frame: the frame to print on
        :return:
        """
        if not self.delete_me:
            frame.draw_sprite((int(self.position[0]), int(self.position[1])),
                              self.sprite, '&', (self.bgcolor, self.fgcolor))

    def respond_to_keypress(self, key):
        """
        Boss does not take any keyboard input,
        therefore a null function in the interface
        """
        return

    def update_on_timestep(self):
        """
        Move the boss into the frame and then make him track the player
        """
        if self.position[1] > self.frame_size[1] - len(self.sprite[0]) - 2:
            self.position = (self.position[0], self.position[1] - 0.2)
        elif self.player.position[0] < self.position[0]:
            self.position = (max(self.position[0] - 0.1, 0), self.position[1])
        elif self.player.position[0] > self.position[0]:
            self.position = (min(
                self.position[0] + 0.1, self.frame_size[0] - len(self.sprite)), self.position[1])
