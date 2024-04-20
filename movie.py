"""..."""

class Movie:
    def __init__(self, title, year, category, is_watched=False):
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        return f"{self.title} - {self.category} ({self.year}) {'*' if not self.is_watched else ''}"

    def watch(self):
        self.is_watched = True

    def unwatch(self):
        self.is_watched = False

    pass
