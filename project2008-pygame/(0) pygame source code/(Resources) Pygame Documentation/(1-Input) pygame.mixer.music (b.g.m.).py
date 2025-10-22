# pygame module for controlling streamed audio
def load(filename): # (filename: str, void)
    # This will load a music filename/file object and prepare it for playback.
    # This does not start the music playing.
    return None

def play(loops=0, start=0.0, fade_ms = 0): # (loops: int, start: float, fade_ms: int)
    # This will play the loaded music stream.
    # If the music is already playing the music will be restarted.
    # The loops argument means how many times to repeat the music. (Set to -1 to make the music repeat indefinately.)
    # The start argument means the position where the music starts playing from.
    # The fade_ms argument make the music start playing at 0 volume and fade up to full volume over the given time.
    return None

def stop(): # (void)
    # Stops the music playback if it is currently playing. (stop)
    return None

def rewind(): # (void)
    # Resets playback of the current music to the beginning. (reset)
    return None

def pause(): # (void)
    # Temporarily stop playback of the music stream. (pause)
    return None

def unpause(): # (void)
    # This will resume the playback of a music stream after it has been paused. (resume)
    return None

def unload(): # (void)
    # This closes resources like files for any music that may be loaded.
    return None

def set_volume(volume): # (volume: float)
    # Set the volume of the music playback
    # The volume argument should be between 0.0 and 1.0
    # When new music is loaded the volume is reset to 1.0
    return None

def get_volume(): # (return: float)
    # Returns the current volume for the mixer
    # The value will be between 0.0 and 1.0
    return float_data