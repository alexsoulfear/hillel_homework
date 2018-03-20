import random
def diff_even_odd(num_limit, lower_bound, upper_bound):# returns int
    even = 0
    odd = 0
    for _ in range (num_limit):
        num_one = random.randint(lower_bound, upper_bound)
        if num_one % 2 == 0:
            even += num_one
        else:
            odd += num_one
        return even - odd


print(diff_even_odd(100, 0, 200))