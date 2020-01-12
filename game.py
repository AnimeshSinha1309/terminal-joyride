"""
Final interface for the game, calls all the modules.
"""

import time
from frame import Frame
from player import Player
from background import Background
import osmanager
from firebeam import FireBeam

FRAME_RATE = 16

# Create the Objects and put them in an array

FRAME = Frame()
PLAYER = Player()
BACKGROUND = Background()
OBJECTS = [BACKGROUND, PLAYER]
TIMESTEP = 0

while True:
    if time.time() > FRAME.previous_render_time + 1 / (2 * FRAME_RATE):
        FRAME.broadcast_input(OBJECTS)  # Get the input to all the objects
    if time.time() > FRAME.previous_render_time + 1 / FRAME_RATE:
        TIMESTEP += 1
        FRAME.broadcast_timestep(OBJECTS)  # Update all object states
        FRAME.broadcast_render(OBJECTS)  # Render objects on the screen cache
        osmanager.clrscr()
        FRAME.render()
        # Initialize the new FireBeams
        NEW_FIREBEAM = FireBeam.spawn((FRAME.rows, FRAME.cols))
        if NEW_FIREBEAM is not False:
            OBJECTS.append(NEW_FIREBEAM)
        if TIMESTEP > PLAYER.last_died + 4:
            for obj in OBJECTS:
                if isinstance(obj, FireBeam) and obj.detect_collision(PLAYER):
                    FRAME.player_die()
                    PLAYER.last_died = TIMESTEP
