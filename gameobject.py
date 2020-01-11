class GameObject:
    """
    Abstract Class describing the features that every object 
    in the game must bear.

    The following methods must be implemented:
    * __init__()
    * __str__()
    * respond_to_keypress(key)
    * update_on_timestep()
    * render_object(frame)
    """

    def __init__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def respond_to_keypress(self, key):
        raise NotImplementedError

    def update_on_timestep(self):
        raise NotImplementedError

    def render_object(self, frame):
        raise NotImplementedError
