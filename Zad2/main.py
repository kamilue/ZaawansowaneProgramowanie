def even_numbers(numbers):
  for number in numbers:
    if number % 2 == 0:
      print(number)

numbers = list(range(92,111))

even_numbers(numbers)