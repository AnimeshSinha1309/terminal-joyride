"""
Final interface for the game, calls all the modules.
"""

import time
import osmanager
from frame import Frame
from player import Player
from background import Background
from firebeam import FireBeam
from boss import Boss
from magnet import Magnet
from coins import Coin
import container

FRAME_RATE = 16

# Create the Objects and put them in an array

FRAME = Frame()
PLAYER = Player()
BACKGROUND = Background()
TIMESTEP = 0
BOSS = None
COINS = [Coin((3, 80))]

# The parts of the game
OBJECTS = [BACKGROUND, PLAYER]
ENDGAME_TIME = 200
MAGNET_TIME = 50

while True:
    # Get the input to all the objects
    if time.time() > FRAME.previous_render_time + 1 / (2 * FRAME_RATE):
        FRAME.broadcast_input(OBJECTS)
    if time.time() > FRAME.previous_render_time + 1 / FRAME_RATE:
        # Update and Render
        TIMESTEP += 1
        FRAME.broadcast_timestep(OBJECTS)
        FRAME.broadcast_render(OBJECTS)
        osmanager.clrscr()
        # Spawn and Process coins
        FRAME.broadcast_timestep(COINS)
        FRAME.broadcast_render(COINS)
        FRAME.render()
        for coin in COINS:
            if not coin.delete_me and coin.detect_collision(PLAYER):
                coin.delete_me = True
                container.score += 1
        # Render the Frame
        FRAME.render()
        # Initialize the new FireBeams and Collision Detect
        if TIMESTEP < ENDGAME_TIME:
            NEW_FIREBEAM = FireBeam.spawn()
            if NEW_FIREBEAM is not False:
                OBJECTS.append(NEW_FIREBEAM)
        if TIMESTEP > PLAYER.last_died + 4:
            for obj in OBJECTS:
                if isinstance(obj, FireBeam) and obj.detect_collision(PLAYER):
                    FRAME.player_die()
                    PLAYER.last_died = TIMESTEP
        # Initialize the Boss Enemy
        if TIMESTEP == ENDGAME_TIME + 5:
            BOSS = Boss(PLAYER)
            OBJECTS.append(BOSS)
        # Check the bullet shootings
        for bullet in PLAYER.bullets:
            if bullet.delete_me:
                continue
            for item in OBJECTS:
                if isinstance(item, FireBeam) and bullet.detect_collision(item):
                    item.delete_me = True
            if BOSS is not None and bullet.detect_collision(BOSS):
                BOSS.die()
        if BOSS is not None:
            for bullet in BOSS.bullets:
                if bullet.delete_me:
                    continue
                if TIMESTEP > PLAYER.last_died + 4 and bullet.detect_collision(PLAYER):
                    PLAYER.last_died = TIMESTEP
                    FRAME.player_die()
        # Create the Magnet
        if TIMESTEP == MAGNET_TIME:
            MAGNET = Magnet(PLAYER)
            OBJECTS.append(MAGNET)
