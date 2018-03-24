import random
def list_creating():
    lst = []
    for _ in range(11):
        lst += [random.randint(-1,1)]
    return lst

lst = list_creating()

def calc_frequency(lst):
    lst_num_1 = lst.count(-1)
    lst_num_2 = lst.count(0)
    lst_num_3 = lst.count(1)
    if lst_num_1 == lst_num_2 or lst_num_1 == lst_num_3 or lst_num_2 == lst_num_3:
        return None
    if lst_num_1 > lst_num_2 and lst_num_1 > lst_num_3:
        return (-1)
    if lst_num_2 > lst_num_1 and lst_num_2 > lst_num_3:
        return (0)
    if lst_num_3 > lst_num_2 and lst_num_3 > lst_num_1:
        return (1)

print(lst)
print(calc_frequency(lst))