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


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        sum_numbers = 0
        for i in self.marks:
            sum_numbers = sum_numbers + i
        avg = sum_numbers / len(self.marks)
        if avg > 50:
            return True
        return False


marks = [1, 2, 3, 5, 2, 4, 5, 6]
marks2 = [51, 55, 53, 22, 67, 60]
marks3 = [351, 155, 53, 1, 2, 60]

library1 = Library('Katowice', 'Adamskiego', '40-000', '15:00', '333476311')
library2 = Library('Żywiec', 'Kościuszki', '34-300', '15:00', '987657122')
employee1 = Employee('Tadeusz', 'Kowalski', '08.06.2016', '02.02.1973', 'Bielsko-Biała', 'Piłsudskiego', '43-300',
                     '535263128')
employee2 = Employee('Marian', 'Kowal', '08.06.2016', '02.02.1973', 'Bielsko-Biała', 'Piłsudskiego', '43-300',
                     '535263128')
employee3 = Employee('Michał', 'Kamiński', '08.06.2016', '02.02.1973', 'Bielsko-Biała', 'Piłsudskiego', '43-300',
                     '535263128')
book1 = Book('Sowa', '20.03.2022', 'Juliusz', 'Słowacki', '301')
book2 = Book('Sowa', '20.03.1882', 'Michał', 'Mickiewicz', '201')
book3 = Book('Lew', '20.03.1932', 'Adam', 'Sienkiewicz', '501')
book4 = Book('Sowa', '05.03.1382', 'Juliusz', 'Głowacki', '301')
book5 = Book('Sowa', '20.03.2021', 'Juliusz', 'Tadeusz', '50')

student1 = Student('Kamil', marks)
student2 = Student('Marcin', marks2)
student3 = Student('Dawid', marks3)

order1 = Order(employee1, student1, book1, '18.10.2022')
order2 = Order(employee3, student3, book4, '10.10.2022')
print(order1)
print(order2)
