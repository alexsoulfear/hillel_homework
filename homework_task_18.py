import random
def sum_symbol_codes(first, last):
    symbol_range = ord(last) - ord(first) + 1
    total = 0
    for i in range (symbol_range):
        total += (ord(first) + i)
    print(total)
    return total

sum_symbol_codes('a', 'z')
