import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
                     
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, valid_ratings, runtime, year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.valid_ratings = valid_ratings
        self.runtime = runtime
        self.year = year

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
