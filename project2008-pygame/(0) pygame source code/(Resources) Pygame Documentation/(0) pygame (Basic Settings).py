# the top level pygame package
def init(): # (return: tuple)
    # Initialize all imported pygame modules
    # No exceptions will be raised if a module fails
    # The total number if successful and failed inits will be returned as a tuple
    # It is a convenient way to get everything started.
    return (numpass, numfail)

def quit(): # (void)
    # Uninitialize all pygame modules that have previously been initialized
    # When the Python interpreter shuts down, this method is automatically called
    # A program does not need it (except when it wants to terminate its pygame resources and continue)
    return None

########################################################################################################################
class Color: # Create a pygame object for color representations
    def __init__(self, color_object): # (color_object: Color)
    def __init__(self, red, green, blue, alpha=255): # (red: int, green: int, blue: int, alpha: int)
    def __init__(self, red, green, blue): # (red: int, green: int, blue: int)
        # Data Attributes
        self.r = red
        self.g = green
        self.b = blue
        self.a = alpha

class Rect: # Create a pygame class for an object storing rectangular coordinates
    def __init__(self, rect_object): # (rect_object: Rect)
    def __init__(self, (left, top), (width, height)): # (left: int, top: int, width: int, height: int)
    def __init__(self, left, top, width, height): # (left: int, top: int, width: int, height: int)
        # Data Attributes
        self.x = left
        self.y = top
        self.w = width
        self.h = height
        self.centerx = left + width / 2
        self.centery = top + height / 2
        self.center = self.centerx, self.centery

    def copy(self): # (return: Rect)
        # Returns a new rectangle having the same position and size as the original
        return rect_object

    def move(self, x, y): # (x: int, y: int, return: Rect)
        # Returns a new rectangle that is moved by the given offset
        return rect_object

    def move_ip(self, x, y): # (x: int, y: int, return: void)
        # Same as the Rect.move() method, but operates by itself
        return None

    def union(self, rect_object): # (rect_object: Rect, return: Rect)
        # Returns a new rectangle that completely covers the area of the two provided rectangles.
        # There may be area inside the new Rect that is not covered by the originals.
        return rect_object

    def union_ip(self, rect_object): # (rect_object: Rect, void)
        # Same as the Rect.union() method, but operates by itself
        return None

    def contains(self, rect_object): # (rect_object: Rect, return: bool)
        # Returns true when the argument is completely inside the Rect.
        return bool_data

    def collidepoint(self, x, y): # (x: int, y: int, return: bool)
        # Returns true if the given point is inside the rectangle (not including the outline)
        return bool_data

    def colliderect(self, rect_object): # (rect_object: Rect, return: bool)
        # Returns true if any portion of either rectangle overlap (except the edges).
        return bool_data

    def collidelist(self, rect_list): # (rect_list: list, return: int)
        # Test whether the rectangle collides with any in a sequence of rectangles.
        # The index of the first collision found is returned.
        # -1 is returned if no collisions are found
        return index

class Surface: # Create a pygame object for representing images
    def __init__(self, (width, height), flags=0, surface_object): # (width: int, height: int, surface_object: Surface)
    def __init__(self, (width, height), flags=0, depth=0, masks=None): # (width: int, height: int)
        # No Data Attributes

    def fill(self, color, rect=None, special_flags=0): # (return: Rect)
        # Fill the Surface with a solid color
        # If no rect argument is given the entire Surface will be filled
        # The rect argument will limit the fill to a specific area
        # The fill will also be contained by the Surface clip area
        return rect_object

    def blit(self, source, dest, area=None, special_flags=0): # (source: Surface, dest: list, return: Rect)
        # Draws a source Surface onto this Surface
        # The draw can be positioned with the dest argument
        return rect_object

    def convert(self, surface_object=None): # (return: Surface)
        # Creates a new copy of the Surface with the pixel format changed
        # goes with pygame.image.load() function
        return surface_object

    def convert_alpha(self): # (return: Surface)
        # Creates a new copy of the Surface with the desired pixel format
        # The new surface will be in a format suited for quick blitting to the given format with per pixel alpha (transparent)
        # goes with pygame.image.load() function
        return surface_object

    def set_alpha(self, value, flags=0): # (value: int, void)
        # Set the current alpha value for the Surface.
        # When blitting this Surface onto a destination, the pixels will be drawn slightly transparent.
        # The alpha value is an integer from 0 to 255, 0 is fully transparent and 255 is fully opaque.
        return None

    def get_rect(self): # (return: Rect)
        # get the rectangular area of the Surface
        # This rectangle will always start at (0, 0) with a width and height the same size as the image.
        # It is used for centering the image
        return rect_object

    def copy(self): # (return: Surface)
        # Makes a duplicate copy of a Surface.
        return surface_object

    def subsurface(self, rect_object): # (rect_object: Rect, return: Surface)
        # Returns a child of the original Surface that shares its pixels with its new parent.
        # Modifications to either Surface pixels will effect each other.
        # The new Surface will inherit the palette, color key, and alpha settings from its parent.
        # It is possible to have any number of subsurfaces and subsubsurfaces on the parent.
        # It is also possible to subsurface the display Surface if the display mode is not hardware accelerated.
        return surface_object