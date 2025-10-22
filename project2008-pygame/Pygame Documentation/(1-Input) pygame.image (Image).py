# pygame module for image transfer
def load(filename): # (return: Surface)
    # Load an image from a file source.
    # The returned Surface will contain the same color format, colorkey and alpha transparency as the file it came from
    # Call convert() method to create a copy that will draw more quickly on the screen.
    # Call convert_alpha() method after loading for alpha transparency of .png images
    return surface_object