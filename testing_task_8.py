def find_and_change(lst):
    min_num = (sorted(lst))[0]
    max_num = (sorted(lst)).pop()
    index_min = []
    index_max = []
    min_counted = lst.count(min_num)
    max_counted = lst.count(max_num)
    for i in range(lst.count(min_num)):
        index_min.append(lst.index(min_num))
        lst.pop(index_min[i])
        lst.insert(index_min[i], 'l')

    for i in range(lst.count(max_num)):
        index_max.append(lst.index(max_num))
        lst.pop(index_max[i])
        lst.insert(index_max[i], 'm')

    for i in range(min_counted):
        lst.pop(index_min[i])
        lst.insert(index_min[i], max_num)

    for i in range(max_counted):
        lst.pop(index_max[i])
        lst.insert(index_max[i], min_num)

    return print(lst)
#тому, кто придумае более извращённый вариант - лично пожму руку.

find_and_change([1, 1, 1, 1, 1, 1])
find_and_change([2, 3, 5, 6, 4, 5, 6])
find_and_change([3, 2, 2, 1, 4, 8, 8, 1, 3, 3, 7, 4, 2])
