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
student = Student('Kamil', marks)
student2 = Student('Marcin', marks2)
print(student.is_passed())
print(student2.is_passed())
