from utils.Book import Book
from utils.Employee import Employee
from utils.Library import Library
from utils.Order import Order
from Persons.Student import Student

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
