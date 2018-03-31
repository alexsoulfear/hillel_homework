def is_closer_to_10 (first_number, second_number):
    first_difference = abs(10 - first_number)
    second_difference = abs(10 - second_number)

    if second_difference > first_difference:
        return print(first_number)
    if second_difference < first_difference:
        return print(second_number)
    if second_difference == first_difference:
        return print(first_number, second_number)

is_closer_to_10(9, 12)
