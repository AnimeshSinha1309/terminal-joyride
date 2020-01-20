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

    bgcolor = cl.Back.BLACK
    fgcolor = cl.Fore.RED

    def __init__(self, player: Player):
        """
        Initialize the boss with the sprite, colors and player to follow
        """
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
        self.position = (int(container.FRAME_ROWS / 2 - 3),
                         container.FRAME_COLS)
        self.player = player
        self.bullets = []
        self.lives = container.BOSS_LIVES

    def render_object(self, frame):
        """
        Implement the way to render on the screen cache
        :param frame: the frame to print on
        """
        if not self.delete_me:
            frame.draw_sprite((int(self.position[0]), int(self.position[1])),
                              self.sprite, '&', (self.bgcolor, self.fgcolor))
            for bullet in self.bullets:
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
        if self.position[1] > container.FRAME_COLS - len(self.sprite[0]) - 2:
            self.position = (
                self.position[0], self.position[1] - container.SCROLL_SPEED)
        else:
            shoot = np.random.choice([False, True], p=[0.9, 0.1])
            for bullet in self.bullets:
                bullet.update_on_timestep()
            if shoot:
                self.bullets.append(EnemyBullet(self.position))
            if self.player.position[0] < self.position[0]:
                self.position = (
                    max(self.position[0] - container.SCROLL_SPEED / 5, 0), self.position[1])
            if self.player.position[0] > self.position[0]:
                self.position = (min(self.position[0] + container.SCROLL_SPEED / 5,
                                     container.FRAME_ROWS - len(self.sprite)),
                                 self.position[1])

    def shoot_bullet(self):
        self.bullets.append(EnemyBullet(self.position))

    def die(self):
        """
        Loses the life for the Boss, ends the game if boss is dead.
        """
        self.lives -= 1
        if self.lives <= 0:
            container.SCORE += 100
            self.delete_me = True
            container.exit_sequence(True)
