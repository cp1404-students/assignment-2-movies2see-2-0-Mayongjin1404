"""..."""


# TODO: Create your MovieCollection class in this file

class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def load_movies(self, filename):
        # Implementation depends on the file format, see the `movies.json` for reference
        pass

    def save_movies(self, filename):
        # Similar to load, save the movies to a JSON file
        pass

    def sort_movies(self, key):
        self.movies.sort(key=lambda movie: getattr(movie, key))

