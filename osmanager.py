"""
System interface to handle the Terminal.
"""

import os
import sys
import select


import termios
import tty
# Changing terminal settings to break on character (getch)
OLD_SETTINGS = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())


def hide_cursor():
    """
    Disables display of the cursor

    Example
    =======
    >>> hide_cursor()
    """
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def show_cursor():
    """
    Enables display of the cursor

    Example
    =======
    >>> show_cursor()
    """
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


def input_available():
    """
    Checks for the availability of an input

    Returns
    =======
    True if there was input, False otherwise

    Note
    ====
    The following preparatory lines in the module load
    are crucial to the working of this method.
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    Example
    =======
    >>> while not input_available():
    >>>     print('.', end='')
    """
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def getch():
    """
    Get the input character asynchronously

    Returns
    =======
    Returns the input character if there was an input, -1 otherwise

    Example
    =======
    >>> while True:
    >>>     c = getch()
    >>>     if c != -1:
    >>>         print(c)
    """
    if input_available():
        character = sys.stdin.read(1)
        return character
    return -1


def clrscr():
    """
    Clears the terminal screen

    Example
    =======
    >>> clrscr()
    """
    os.system('clear')


def sys_exit():
    """
    Exits out to the system, undoing all changes to the terminal done for the game

    Example
    =======
    >>> sys_exit()
    """
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, OLD_SETTINGS)
    show_cursor()
    exit(0)


class LogWriter:
    """
    Helper class to write logs
    """

    @staticmethod
    def verbose(log):
        """
        Writes the verbose log file
        :param log: string to be logged
        :return:
        """
        with open('verbose.log', 'w+') as file:
            file.write(log)

    @staticmethod
    def message(log):
        """
        Writes the message log file
        :param log: string to be logged
        :return:
        """
        with open('message.log', 'w+') as file:
            file.write(log)

    @staticmethod
    def error(log):
        """
        Writes the error log file
        :param log: string to be logged
        :return:
        """
        with open('error.log', 'w+') as file:
            file.write(log)


if __name__ == '__main__':
    for i in range(100000000000):
        print(i)
        c = getch()
        if c == 'q':
            break
        elif c != -1:
            print(c)
            input()
    sys_exit()
