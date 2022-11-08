from Classes.Student import Student

marks = [1, 2, 3, 5, 2, 4, 5, 6]
marks2 = [51, 55, 53, 22, 67, 60]
student = Student('Kamil', marks)
student2 = Student('Marcin', marks2)
print(student.is_passed())
print(student2.is_passed())
