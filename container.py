"""
Contains Global constants that need to be synced across all modules
(or sometimes variables - not recommended)
"""

import osmanager

FRAME_ROWS, FRAME_COLS = 24, 80
FRAME_SIZE = (FRAME_ROWS, FRAME_COLS)

MAGNET_LIFE = 200
SCROLL_SPEED = 0.5
ENDGAME_TIME = 600
BOSS_DELAY = 220
DROGON_DELAY = 30
DROGON_LIFE = 200

MAGNET_TIME = 200
SHIELD_LIFE = 50
SHIELD_REFILL = 300
SPEEDUP_LIFE = 50
SPEEDUP_REFILL = 300
BOSS_LIVES = 200

SHEILD_UP = False
SCORE = 0
LIVES = 10
TIME_REMAINING = 2000


def exit_sequence(won: bool):
    """
    Exits from the game gracefully
    """
    osmanager.clrscr()
    if won:
        print("You Win, You saved baby Yoda, Yay!")
    else:
        print("You Lose")
    print("Score =", SCORE)
    input()
    osmanager.clrscr()
    osmanager.sys_exit()
