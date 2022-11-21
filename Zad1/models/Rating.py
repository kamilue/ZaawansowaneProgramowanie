class Rating:
    @property
    def user_id(self):
        return self._user_id

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def rating(self):
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp

    def __init__(
            self, user_id: int, movie_id: int, rating: float, timestamp: str
    ):
        self._user_id = user_id
        self._movie_id = movie_id
        self._rating = rating
        self._timestamp = timestamp

    def __str__(self):
        return f'"user_id": {self._user_id},"movie_id": "{self._movie_id}", \
            "rating": "{self._rating}", "timestamp": "{self._timestamp}"'

    def __dict__(self):
        return {
            "user_id": self._user_id,
            "movie_id": self._movie_id,
            "rating": self._rating,
            "timestamp": f"{self._timestamp}",
        }
