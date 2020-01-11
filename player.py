from person import Person
from frame import Frame
import colorama as cl


class Player(Person):
    """
    Properties
    ==========
    Lives: int, lives left with the player
    Score: int, score of the player
    Position: (row, col) index of the top left corner of sprite
    Velocity: int, velocity
    """

    def __init__(self):
        self.score = 0
        self.lives = 3
        self.position = (20, 4)
        self.sprite = [
            " O ",
            "/|\\",
            "/ \\"
        ]
        self.bgcolor = cl.Back.RED
        self.fgcolor = cl.Fore.WHITE
        self.zindex = 100

    def __str__(self):
        return "\n".join(self.sprite)

    def render_object(self, frame: Frame):
        frame.draw_sprite(self.position, self.sprite, ' ',
                          self.bgcolor, self.fgcolor)

    def respond_to_keypress(self, key):
        if key == 'a':
            self.position = (self.position[0], max(self.position[1] - 1, 2))
        elif key == 'd':
            self.position = (self.position[0], min(self.position[1] + 1, 60))
        if key == 'a':
            self.position = (max(self.position[0] + 3, 1), self.position[1])

    def update_on_timestep(self):
        return
        y_coord = min(self.position[0] + 1, 20)
        self.position = (y_coord, self.position[1])


if __name__ == '__main__':
    p = Player()
    print(p)
