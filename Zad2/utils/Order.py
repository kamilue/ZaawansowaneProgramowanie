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
