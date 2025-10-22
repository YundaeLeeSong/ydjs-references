class Sound: # Create a new Sound object from a file or buffer object
    def __init__(self, filename): # (filename: str)
        # No Data Attributes

    def play(self, loops=0, maxtime=0, fade_ms=0): # (return: Channel)
        # Begin playback of the Sound on an available Channel.
        # The loops argument controls how many times the sample will be repeated
        # the Sound will loop indefinitely if loops is set to -1
        # The maxtime argument can be used to stop playback after a given number of milliseconds
        # The fade_ms argument will make the sound start playing at 0 volume and fade up to full volume over the time given.
        # This returns the Channel object for the channel that was selected.
        return channel_object

    def stop(self): # (void)
        # This will stop the playback of this Sound on any active Channels.
        return None

    def fadeout(time): # (time: int, void)
        # This will stop playback of the sound after fading it out over the time argument in milliseconds.
        return None

    def set_volume(self, value): # (value: float)
        # This will set the playback volume (loudness) for this Sound in the range of 0.0 to 1.0
        # This will immediately affect the Sound if it is playing
        return None