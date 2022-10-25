def every_second_element(values):
    second_values = []

    for index in range(1, len(values), 2):
        second_values.append(values[index])

    print(second_values)


numbers = list(range(92, 111))

every_second_element(numbers)
