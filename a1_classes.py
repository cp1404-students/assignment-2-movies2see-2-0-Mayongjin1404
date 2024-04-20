"""..."""
# TODO: Copy your first assignment to this file, then update it to use Movie class

from movie import Movie
from moviecollection import MovieCollection

def show_menu():
    """Display the main menu and handle user choices."""
    movies = MovieCollection()
    movies.load_movies(FILENAME)
    menu = "\nMenu:\nD - Display movies\nA - Add new movie\nW - Watch a movie\nQ - Quit\n"
    
    while True:
        print(menu)
        choice = input(">>> ").upper()
        if choice == "D":
            movies.display_movies()
        elif choice == "A":
            title = input("Title: ")
            category = input("Category: ")
            year = input("Year: ")
            if year.isdigit():
                movies.add_movie(Movie(title, int(year), category))
                print(f"{title} added.")
            else:
                print("Invalid year. Please enter a valid number.")
        elif choice == "W":
            movies.display_movies()
            try:
                choice = int(input("Enter the number of a movie to mark as watched: "))
                if 0 <= choice < len(movies.movies):
                    movies.movies[choice].watch()
                    print(f"{movies.movies[choice].title} from {movies.movies[choice].year} watched")
                else:
                    print("Invalid selection or movie already watched.")
            except ValueError:
                print("Invalid input; please enter a valid number.")
        elif choice == "Q":
            movies.save_movies(FILENAME)
            print("Movies saved. Have a nice day :)")
            break
        else:
            print("Invalid menu choice")

if __name__ == "__main__":
    print("Movies2See 2.0 - Welcome")
    show_menu()
