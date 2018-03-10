def sum_of_digits_str (number_str):
    sum_str = (int(number_str[0])) + (int(number_str[1])) + (int(number_str[2]))
    return int(sum_str)

print (sum_of_digits_str("346"))

def sum_of_digits_int (number_int):
    sum_int = (int(number_int % 10)) + (int((number_int% 100) // 10)) + (int((number_int % 1000) // 100))
    return sum_int

print (sum_of_digits_int(346))