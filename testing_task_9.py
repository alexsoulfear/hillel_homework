def normalize (number_lst):
    max_num = 0
    if abs(sorted(number_lst)[0]) > int((sorted(number_lst)).pop()):
        max_num = abs(sorted(number_lst)[0])
    else:
        max_num = int((sorted(number_lst)).pop())

    for i in range(3):
        extr = number_lst[i]
        number_lst.pop(i)
        number_lst.insert(i, (extr / max_num))
    return print(number_lst)

normalize([-5, 3, 4])