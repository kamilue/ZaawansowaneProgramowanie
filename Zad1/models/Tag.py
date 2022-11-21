class Tag:
    @property
    def user_id(self):
        return self._user_id

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def tag(self):
        return self._tag

    @property
    def timestamp(self):
        return self._timestamp

    def __init__(self, user_id: int, movie_id: int, tag: str, timestamp: str):
        self._user_id = user_id
        self._movie_id = movie_id
        self._tag = tag
        self._timestamp = timestamp

    def __str__(self):
        return f'"user_id": {self._user_id},"movie_id": "{self._movie_id}", \
            "tag": "{self._tag}", "timestamp": "{self._timestamp}"'

    def __dict__(self):
        return {
            "user_id": self._user_id,
            "movie_id": self._movie_id,
            "tag": f"{self._tag}",
            "timestamp": f"{self._timestamp}",
        }
