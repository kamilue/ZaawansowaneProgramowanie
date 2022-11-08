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
