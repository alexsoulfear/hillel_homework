def fibonaci_nums_sum(leingth_of_the_string):
    fibonaci_nums = ['1', '1']
    sum = 0
    for i in range(leingth_of_the_string - 2):
        fibonaci_nums += [str((int(fibonaci_nums[i + 1])) + (int(fibonaci_nums[i])))]
    for i in range(leingth_of_the_string):
        sum += int(fibonaci_nums[i])
    return print(sum)

fibonaci_nums_sum(10)