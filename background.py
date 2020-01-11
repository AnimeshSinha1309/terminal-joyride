from gameobject import GameObject
from frame import Frame
import colorama as cl


class Background(GameObject):

    def __init__(self):
        pass

    def respond_to_keypress(self, key):
        pass

    def update_on_timestep(self):
        pass

    def render_object(self, frame):
        frame.draw_rect(0, frame.ROWS, 0, frame.COLS,
                        ' ', bgcolor=cl.Back.CYAN)
        frame.draw_rect(frame.ROWS - 1, frame.ROWS, 0,
                        frame.COLS, ' ', bgcolor=cl.Back.GREEN)
