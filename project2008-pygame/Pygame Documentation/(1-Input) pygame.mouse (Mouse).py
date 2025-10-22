# pygame module to work with the mouse
def get_pressed(): # (return: tuple)
    # get the state of the mouse buttons
    # Returns a sequence of booleans representing the state of all the mouse buttons.
    # A true value means the mouse is currently being pressed at the time of the call.
    return (bool_data_1, bool_data_2, bool_data_3)

def get_pos(): # (return: tuple)
    # Returns the X and Y position of the mouse cursor
    return (x, y)