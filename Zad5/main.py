def check_if_equal_parameters(value: list, number: int) -> bool:
    for i in range(len(value)):
        if value[i] == number:
            return True
        return False

list = 1,2,3,45
number = 1

check_if_equal_parameters(list,number)