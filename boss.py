"""
Implement the Boss Enemy at the end of the game.
"""

import colorama as cl
import numpy as np
import container
from person import Person
from player import Player
from bullets import EnemyBullet


class Boss(Person):
    """
    Final Boss of the game, he follows you around and shoots at you
    """

    _bgcolor = cl.Back.BLACK
    _fgcolor = cl.Fore.RED

    def __init__(self, player: Player):
        """
        Initialize the boss with the _sprite, colors and player to follow
        """
        self._sprite = [
            "&&&&.----.__ &",
            "&&&/---.__  \\&",
            "&&/       `\\ |",
            "&| o     o  \\|",
            "/| .vvvvv.  |\\",
            "/| |     |  |\\",
            "&| `^vvvv'  |&",
            "&\\__________|&"
        ]
        self._position = (int(container.FRAME_ROWS / 2 - 3),
                          container.FRAME_COLS)
        self._player = player
        self._bullets = []
        self.lives = container.BOSS_LIVES

    def render_object(self, frame):
        """
        Implement the way to render on the screen cache
        :param frame: the frame to print on
        """
        if not self._delete_me:
            frame.draw_sprite((int(self._position[0]), int(self._position[1])),
                              self._sprite, '&', (self._bgcolor, self._fgcolor))
            for bullet in self._bullets:
                bullet.render_object(frame)

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
        if self._position[1] > container.FRAME_COLS - len(self._sprite[0]) - 2:
            self._position = (
                self._position[0], self._position[1] - container.SCROLL_SPEED)
        else:
            shoot = np.random.choice([False, True], p=[0.9, 0.1])
            for bullet in self._bullets:
                bullet.update_on_timestep()
            if shoot:
                self._bullets.append(EnemyBullet(self._position))
            if self._player.position[0] < self._position[0]:
                self._position = (
                    max(self._position[0] - container.SCROLL_SPEED / 5, 0), self._position[1])
            if self._player.position[0] > self._position[0]:
                self._position = (min(self._position[0] + container.SCROLL_SPEED / 5,
                                      container.FRAME_ROWS - len(self._sprite)),
                                  self._position[1])

    def shoot_bullet(self):
        self._bullets.append(EnemyBullet(self._position))

    def die(self):
        """
        Loses the life for the Boss, ends the game if boss is dead.
        """
        self.lives -= 1
        if self.lives <= 0:
            container.SCORE += 100
            self._delete_me = True
            container.exit_sequence(True)
