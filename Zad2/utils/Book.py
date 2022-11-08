class Book:
    library: str
    publication_date: str
    author_name: str
    author_surname: str
    number_of_pages: str

    def __init__(self, library,
                 publication_date,
                 author_name,
                 author_surname,
                 number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages


def __str__(self):
    return f'In this class are props about Book and there is library object'
