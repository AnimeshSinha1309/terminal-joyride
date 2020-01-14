"""
Contains Global constants that need to be synced across all modules
(or sometimes variables - not recommended)
"""

import osmanager

FRAME_ROWS, FRAME_COLS = 24, 80
FRAME_SIZE = (FRAME_ROWS, FRAME_COLS)

MAGNET_LIFE = 200
SCROLL_SPEED = 0.5
ENDGAME_TIME = 500

MAGNET_TIME = 200
SHIELD_LIFE = 20
SPEEDUP_LIFE = 20

SHEILD_UP = False
SCORE = 0


def exit_sequence(won: bool):
    """
    Exits from the game gracefully
    """
    osmanager.clrscr()
    if won:
        print("You Win")
    else:
        print("You Lose")
    print("Score =", SCORE)
    input()
    osmanager.clrscr()
    osmanager.sys_exit()
