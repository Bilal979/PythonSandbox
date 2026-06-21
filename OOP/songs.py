class Songs:
    """
    Class to represent a song
    Attributes:
        title (str): The title of the song
        artist (str): The artist of the song
        duration (int): The duration of the song in seconds

    """

    def __init__(self, title, artist, duration):
        """
        The constructor for the Song class
        Attributes:
            title (str): The title of the song
            artist (str): The artist of the song
            duration (int): The duration of the song in seconds
        """
        self.title = title
        self.artist = artist
        self.duration = duration


# help(Songs)
help(Songs.__init__)