import os
import sys
import select


if os.name == 'nt':
    import msvcrt
    import ctypes

    # Registering cursor status to the MS terminal
    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

elif os.name == 'posix':
    import termios
    import tty
    # Changing terminal settings to break on character (getch)
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())


def hide_cursor():
    """
    Disables display of the cursor

    Example
    =======
    >>> hide_cursor()
    """
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()


def show_cursor():
    """
    Enables display of the cursor

    Example
    =======
    >>> show_cursor()
    """
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
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
    if os.name == 'nt':
        return msvcrt.kbhit()
    elif os.name == 'posix':
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
    if os.name == 'posix':
        if input_available():
            c = sys.stdin.read(1)
            return c
        else:
            return -1
    elif os.name == 'nt':
        if msvcrt.kbhit():
            return msvcrt.getch()
        else:
            return -1


def clrscr():
    """
    Clears the terminal screen

    Example
    =======
    >>> clrscr()
    """
    _ = os.system('cls') if os.name == 'nt' else os.system('clear')


def sys_exit():
    """
    Exits out to the system, undoing all changes to the terminal done for the game

    Example
    =======
    >>> sys_exit()
    """
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    show_cursor()
    exit(0)


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
