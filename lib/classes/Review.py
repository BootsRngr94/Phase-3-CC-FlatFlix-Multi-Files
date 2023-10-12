class Review:
    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        self.movie._reviews.append(self)
        self.movie._viewers.append(self.viewer)

        self.viewer._reviews.append(self)
        self.viewer._movies.append(self.movie)
        Review.all.append(self)
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, new_rating):
        if hasattr(self, '_rating'):
            raise Exception("Rating cannot be changed after initialization")
        if isinstance(new_rating, int) and 1 <= new_rating <= 5:
            self._rating = new_rating
        else:
            raise Exception("Rating must be an integer between 1 and 5")
        

