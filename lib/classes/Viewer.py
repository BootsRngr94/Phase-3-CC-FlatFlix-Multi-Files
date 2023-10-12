from classes.Review import Review
class Viewer:
    def __init__(self, username):
        self.username = username
        self._reviews = []
        self._movies = []
        

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if type(username) == str and 6 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Name must be a string greater than 0 characters!")

    def reviews(self):
        return self._reviews

    def reviewed_movies(self):
        return list(set(self._movies))

    def has_reviewed_movie(self, movie):
        return any(review.movie == movie for review in self._reviews)


    def add_review(self, movie, rating):
        new_review = Review(self, movie, rating)
        return new_review