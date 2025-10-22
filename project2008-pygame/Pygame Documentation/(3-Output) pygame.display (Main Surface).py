# pygame module to control the display window and screen
def init(): # (return: void)
    # Initialize the display module (Repeated calls have no effect)
    # The display module cannot do anything until it is initialized
    # (!) Not needed due to the init method in pygame module
    return None

def quit(): # (return: void)
    # Uninitialize the display module
    # Any active displays will be closed
    # (!) Not needed due to the quit method in pygame module
    return None

def set_mode(size=(0, 0), flags=0, depth=0, display=0): # (size: list, return: Surface)
    # Initialize a screen for display (Main Surface Object)
    # The size argument is a pair of numbers representing the width and height
    # The flags argument controls which type of display you want (Combination of ultiple types can be done by | character)
        # pygame.FULLSCREEN    create a fullscreen display
        # pygame.DOUBLEBUF     recommended for HWSURFACE or OPENGL
        # pygame.HWSURFACE     hardware accelerated, only in FULLSCREEN
        # pygame.OPENGL        create an OpenGL-renderable display
        # pygame.RESIZABLE     display window should be sizeable
        # pygame.NOFRAME       display window will have no border or controls
        # pygame.SCALED        resolution depends on desktop size and scale graphics
    # Do not pass the depth and display arguments
    return surface_object

def set_icon(surface_object): # (surface_object: Surface, return: void)
    # Sets the runtime icon on the window (Most systems want a image around 32x32)
    return None

def set_caption(title, icontitle=None): # (title: str, return: void)
    # Sets the name on the window
    return None

def update(rectangle=None): # (return: void)
    # It allows only a portion of the main screen to updated, instead of the entire area
    # If no argument is passed it updates the entire Surface area of the main surface
    return None