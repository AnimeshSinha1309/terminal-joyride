from frame import Frame
from player import Player
from background import Background
import osmanager
import time

FRAME_RATE = 5

# Create the Objects and put them in an array

fr = Frame()
pl = Player()
bg = Background()
objects = [bg, pl]

while True:
    if time.time() > fr.previous_render_time + 1 / FRAME_RATE:
        fr.broadcast_input(objects)  # Get the input to all the objects
        fr.broadcase_timestep(objects)  # Update all object states
        # Render all the objects on the screen cache
        fr.broadcast_render(objects)
        osmanager.clrscr()
        fr.render()
