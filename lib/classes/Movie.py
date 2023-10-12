
class Movie:
    def __init__(self, title):
        self.title = title
        self._reviews = []
        self._viewers = []
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception("Name must be a string greater than 0 characters!")
        

    def reviews(self):
        return self._reviews

    def reviewers(self):
        return list(set(self._viewers))

    def average_rating(self):
        if not self._reviews:
            return None

        total_ratings = sum(review.rating for review in self._reviews)
        average = round(total_ratings / len(self._reviews), 1)
        return average