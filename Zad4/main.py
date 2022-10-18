def check_sum(number1: int, number2: int, number3: int) -> bool:
    sum = number1 + number2
    if sum >= number3:
        return True
    else:
        return False

check_sum(1,2,4)