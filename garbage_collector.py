"""
Implemets any garbage collection features to keep memory light
"""

LAST_RUN_TIME = -1000


def garbage_collect(data):
    """
    Takes the array and actually delete all already deleted object
    so that the python garbage collector can wrap it up.
    :param data: list of all objects where some have to be deleted
    """
    return [el for el in data if not el.delete_me]
