import random
def diff_min_max(num_limit, lower_bound, upper_bound):
    max_num = lower_bound
    min_num = upper_bound
    for _ in range (num_limit):
        number = random.randint(lower_bound,upper_bound)
        print(number)
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number - 1
    return max_num, min_num, max_num - min_num

print(diff_min_max(9, 0, 15))
