import webbrowser
import video

class Movie(video.Video):
    """ This class provides a way to store movie related information """
    
    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self, movie_title, duration, movie_storyline, movie_image, movie_trailer):
        video.Video.__init__(self,movie_title,duration)
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.youtube_trailer_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)