def is_closer_to_10 (first_number, second_number):
    first_difference = 0
    second_difference = 0
    if first_number >= 10:
        first_difference = first_number - 10
    if first_number <= 10:
        first_difference = 10 - first_number

    if second_number >= 10:
        second_difference = second_number - 10
    if second_number <= 10:
        second_difference = 10 - second_number

    if second_difference > first_difference:
        return print(first_number)
    if second_difference < first_difference:
        return print(second_number)
    if second_difference == first_difference:
        return print(first_number, second_number)

is_closer_to_10(9, 12)