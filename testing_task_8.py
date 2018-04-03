def find_and_change(lst):
    min_num = (sorted(lst))[0]
    max_num = (sorted(lst)).pop()
    return print(min_num, max_num)

find_and_change([1, 1, 1, 1, 1, 1])
find_and_change([2, 3, 5, 6, 4, 5, 6])
find_and_change([3, 2, 2, 1, 4, 8, 8, 1, 3, 3, 7, 4, 2])