# pygame module for loading and rendering fonts
def init(): # (return: void)
    # Initializes the font module
    # The module must be initialized before any other functions will work
    # (!) Not needed due to the init method in pygame module
    return None

def quit(): # (return: void)
    # uninitialize the font module
    # (!) Not needed due to the quit method in pygame module
    return None

def get_fonts(): # (return: list)
    # Returns a list of all the fonts available on the system.
    # Sometimes return an empty list if the system cannot find fonts.
    return strings_list

def SysFont(name, size, bold=False, italic=False): # (name: str, size: int, return: Font)
    # Return a new Font object that is loaded from the system fonts
    # The font will match the requested bold and italic flags
    # If a suitable system font is not found, the system will use the default pygame font
    return font_object

########################################################################################################################
class Font: # Create a new Font object from a file
    def __init__(filename, size): # (filename: Font)
    def __init__(object, size): # (object: int, size: int)
        # No Data Attributes

    def render(text, antialias, color, background=None): # (return: Surface)
        # This creates a new Surface with the specified text rendered on it. pygame provides no way to directly draw text on an existing Surface: instead you must use Font.render() to create an image (Surface) of the text, then blit this image onto another Surface.
        #
        # The text can only be a single line: newline characters are not rendered. Null characters ('x00') raise a TypeError. Both Unicode and char (byte) strings are accepted. For Unicode strings only UCS-2 characters ('u0001' to 'uFFFF') are recognized. Anything greater raises a UnicodeError. For char strings a LATIN1 encoding is assumed. The antialias argument is a boolean: if true the characters will have smooth edges. The color argument is the color of the text [e.g.: (0,0,255) for blue]. The optional background argument is a color to use for the text background. If no background is passed the area outside the text will be transparent.
        #
        # The Surface returned will be of the dimensions required to hold the text. (the same as those returned by Font.size()). If an empty string is passed for the text, a blank surface will be returned that is zero pixel wide and the height of the font.
        #
        # Depending on the type of background and antialiasing used, this returns different types of Surfaces. For performance reasons, it is good to know what type of image will be used. If antialiasing is not used, the return image will always be an 8-bit image with a two-color palette. If the background is transparent a colorkey will be set. Antialiased images are rendered to 24-bit RGB images. If the background is transparent a pixel alpha will be included.
        #
        # Optimization: if you know that the final destination for the text (on the screen) will always have a solid background, and the text is antialiased, you can improve performance by specifying the background color. This will cause the resulting image to maintain transparency information by colorkey rather than (much less efficient) alpha values.
        #
        # If you render '\n' an unknown char will be rendered. Usually a rectangle. Instead you need to handle new lines yourself.
        #
        # Font rendering is not thread safe: only a single thread can render text at any time.
        return rect_object