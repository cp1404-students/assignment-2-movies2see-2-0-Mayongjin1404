"""(Incomplete) Tests for MovieCollection class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies, 

    # Test loading movies
    print("\nTest loading movies:")
    movie_collection.load_movies("movies.json")  
    print(movie_collection)
    assert movie_collection.movies, "Movies should be loaded"

    # Test adding a new Movie with values
    print("\nTest adding new movie:")
    new_movie = Movie("Amazing Grace", 2006, "Drama", False)
    movie_collection.add_movie(new_movie)
    assert new_movie in movie_collection.movies, 
    print(movie_collection)

    # Test sorting movies by year
    print("\nTest sorting - year:")
    movie_collection.sort_movies('year')  
    if len(movie_collection.movies) > 1:
        assert movie_collection.movies[0].year <= movie_collection.movies[1].year, 
    print(movie_collection)

    # Test sorting movies by title
    print("\nTest sorting - title:")
    movie_collection.sort_movies('title')
    if len(movie_collection.movies) > 1:
        assert movie_collection.movies[0].title <= movie_collection.movies[1].title, 
    print(movie_collection)

    # Test saving movies
    print("\nTest saving movies:")
    movie_collection.save_movies("movies_test_output.json")  
    print("Movies saved to 'movies_test_output.json'. Please check this file manually.")

if __name__ == '__main__':
    run_tests()

