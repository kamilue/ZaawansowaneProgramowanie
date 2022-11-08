def merge_lists(list1: list, list2: list) -> list:
    merged_list = list(set(list1 + list2))
    squared_numbers = [number ** 3 for number in merged_list]
    return squared_numbers
