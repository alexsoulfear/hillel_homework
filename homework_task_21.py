def get_max_digit(number): # returns int
    numb = list(str(number))
    maximum = 0
    num = -1
    for _ in range(12):
        num += 1
        if int(numb[num]) > maximum:
            maximum = (maximum - maximum) + int(numb[num])
        else:
            pass
    return maximum
print(get_max_digit(324232123122))