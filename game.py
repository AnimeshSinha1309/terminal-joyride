"""
Final interface for the game, calls all the modules.
"""

import time
from frame import Frame
from player import Player
from background import Background
import osmanager

FRAME_RATE = 5

# Create the Objects and put them in an array

FRAME = Frame()
PLAYER = Player()
BACKGROUND = Background()
OBJECTS = [BACKGROUND, PLAYER]

while True:
    if time.time() > FRAME.previous_render_time + 1 / FRAME_RATE:
        FRAME.broadcast_input(OBJECTS)  # Get the input to all the objects
        FRAME.broadcast_timestep(OBJECTS)  # Update all object states
        FRAME.broadcast_render(OBJECTS)  # Render objects on the screen cache
        osmanager.clrscr()
        FRAME.render()
