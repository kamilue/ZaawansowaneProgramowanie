def check_if_even(number: int) -> bool:
    even_number = number % 2 == 0

    if even_number:
        print(f'Liczba parzysta')
    else:
        print(f'Liczba nieparzysta')

number = 5

check_if_even(number)