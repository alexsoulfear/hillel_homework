import random
def diff_min_max(num_limit, lower_bound, upper_bound):
    max_num = upper_bound
    min_num = lower_bound
    for _ in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        if number > min_num:
            max_num = number
        else:
            min_num = number
    return max_num - min_num

print(diff_min_max(9, 0, 15))