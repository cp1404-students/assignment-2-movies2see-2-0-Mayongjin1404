"""(Incomplete) Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")

    default_movie = Movie()
    print(default_movie)  # Expected output will depend on how __str__ is defined
    assert default_movie.title == "", "Title should be empty"
    assert default_movie.category == "", "Category should be empty"
    assert default_movie.year == 0, "Year should be 0"
    assert not default_movie.is_watched, "Movie should not be watched"

    # Test initial-value movie
    print("\nTest initial-value movie:")
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    print(initial_movie)
    assert initial_movie.title == "Thor: Ragnarok", "Title should be 'Thor: Ragnarok'"
    assert initial_movie.year == 2017, "Year should be 2017"
    assert initial_movie.category == "Comedy", "Category should be 'Comedy'"
    assert initial_movie.is_watched, "Movie should be watched"

    # Test the watch and unwatch methods
    print("\nTesting watch and unwatch methods:")
    movie_to_watch = Movie("The Avengers", 2012, "Action")
    print("Before watch:", movie_to_watch)
    movie_to_watch.watch()
    assert movie_to_watch.is_watched, "Movie should be marked as watched"
    print("After watch:", movie_to_watch)

    movie_to_watch.unwatch()
    assert not movie_to_watch.is_watched, "Movie should be marked as unwatched"
    print("After unwatch:", movie_to_watch)

    # Test string representation
    print("\nTesting string representation:")
    movie_str = Movie("Inception", 2010, "Thriller", False)
    expected_str = "*Inception - Thriller (2010)"
    actual_str = str(movie_str)
    print("Expected:", expected_str)
    print("Actual:", actual_str)
    assert actual_str == expected_str, "String representation should match expected output"

if __name__ == '__main__':
    run_tests()

