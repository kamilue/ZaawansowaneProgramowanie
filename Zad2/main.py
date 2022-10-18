class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str


def __init__(self, city, street, zip_code, open_hours, phone):
    self.city = city
    self.street = street
    self.zip_code = zip_code
    self.open_hours = open_hours
    self.phone = phone


def __str__(self):
    return f'In this class are props about Library'


class Employee:
    first_name: str
    last_name: str
    hire_date: str
    birth_date: str
    city: str
    street: str
    zip_code: str
    phone: str


def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
    self.first_name = first_name
    self.last_name = last_name
    self.hire_date = hire_date
    self.birth_date = birth_date
    self.city = city
    self.street = street
    self.zip_code = zip_code
    self.phone = phone


def __str__(self):
    return f'In this class are props about Employee'


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


class Order:
    employee: str
    student: str
    books: list
    order_date: str


def __init__(self, employee,
             student,
             books,
             order_date):
    self.employee = employee
    self.student = student
    self.books = books
    self.order_date = order_date


def __str__(self):
    return f'In this class are props about Order'
