"""
Name:Ma Yongjin
Date:04.20.2024
Brief Project Description:need to integrate various components including loading and saving movies, displaying them, and handling user interactions
GitHub URL:https://github.com/cp1404-students/assignment-2-movies2see-2-0-Mayongjin1404
"""
# TODO: Create your main program in this file, using the Movies2SeeApp class

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

from movie import Movie
from moviecollection import MovieCollection

class Movies2SeeApp(App):
    def build(self):
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies('movies.json')

        self.root = BoxLayout(orientation='vertical')
        
        # Top part for displaying movies
        self.movie_list = BoxLayout(size_hint_y=None, height=30, orientation='horizontal')
        self.update_movie_list()
        self.root.add_widget(self.movie_list)

        # Middle part for user input
        self.input_area = BoxLayout(size_hint_y=None, height=30)
        self.title_input = TextInput(hint_text='Title', size_hint_x=None, width=200)
        self.year_input = TextInput(hint_text='Year', size_hint_x=None, width=100)
        self.category_input = Spinner(
            text='Category',
            values=('Action', 'Comedy', 'Documentary', 'Drama', 'Fantasy', 'Thriller'),
            size_hint_x=None,
            width=100
        )
        self.add_movie_button = Button(text='Add Movie', on_press=self.add_movie)
        self.input_area.add_widget(self.title_input)
        self.input_area.add_widget(self.year_input)
        self.input_area.add_widget(self.category_input)
        self.input_area.add_widget(self.add_movie_button)
        self.root.add_widget(self.input_area)

        # Bottom part for status messages
        self.status_label = Label(size_hint_y=None, height=30)
        self.root.add_widget(self.status_label)

        return self.root

    def update_movie_list(self):
        self.movie_list.clear_widgets()
        for movie in self.movie_collection.movies:
            btn = Button(text=str(movie), on_press=self.toggle_watch_status)
            btn.movie = movie  # Storing movie object in button for easy access
            self.movie_list.add_widget(btn)

    def add_movie(self, instance):
        title = self.title_input.text
        year = self.year_input.text
        category = self.category_input.text
        if not title or not year.isdigit() or category not in self.category_input.values:
            self.status_label.text = 'Invalid input. Please check your data.'
            return
        movie = Movie(title, int(year), category)
        self.movie_collection.add_movie(movie)
        self.update_movie_list()
        self.status_label.text = 'Movie added successfully.'

    def toggle_watch_status(self, instance):
        movie = instance.movie
        movie.watch() if not movie.is_watched else movie.unwatch()
        instance.text = str(movie)  # Update button text
        self.status_label.text = f'Movie status changed: {movie.title}'

    def on_stop(self):
        self.movie_collection.save_movies('movies.json')

if __name__ == '__main__':
    Movies2SeeApp().run()
