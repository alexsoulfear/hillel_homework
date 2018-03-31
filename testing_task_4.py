def count (number5numeric):
    total = 1
    for i in range (len(str(number5numeric))):
        number = int((str(number5numeric))[i])
        if number % 2 == 0:
            total *= number
    return print(total)

count(32323)
