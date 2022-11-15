class Movie:
    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def genres(self):
        return self._genres

    def __init__(self, id: int, title: str, genres: str):
        self._id = id
        self._title = title
        self._genres = genres

    def __str__(self):
        return f'"id": {self._id},"title": "{self._title}", \
            "genres": "{self._genres}"'

    def __dict__(self):
        return {
            "id": self._id,
            "title": f"{self._title}",
            "genres": f"{self._genres}",
        }
