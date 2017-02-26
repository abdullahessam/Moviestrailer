import webbrowser
class Movie:
    """...this class used to store Movies..."""
    def __init__(self,title,storyline,poster,youtube):
        """[this function used as a constructor to the class Movie to store Movies details]"""
        self.title=title
        self.movie_Story=storyline
        self.poster_image_url=poster
        self.trailer_youtube_url=youtube

    def open_trailer(self):
        webbrowser.open(self.movie_youtupe)

