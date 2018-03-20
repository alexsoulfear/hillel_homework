import random
def diff_min_max(num_limit, lower_bound, upper_bound):
    fst_num = random.randint(lower_bound, upper_bound)
    scd_num = random.randint(lower_bound, upper_bound)
    for _ in range (num_limit):
        if fst_num > scd_num:
            return fst_num - scd_num
        else:
            return scd_num - fst_num
    return int

print(diff_min_max(9, 0, 15))