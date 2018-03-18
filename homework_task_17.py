import math
def solve_quadratic_equation(a, b, c):# 10, 2, 0
    descr = (b ** 2) - (4 * a * c)# 4 - 0
    def values_pl (a, b):
        value_2 = (-b + math.sqrt(descr)) / (a * 2)
        value_1 = (-b - math.sqrt(descr)) / (a * 2)
        return value_2,value_1
    def value_zer (a, b):
        value = (-b) / (a * 2)
        return value
    if descr > 0:
        return values_pl(a, b)
    else:
        if descr == 0:
            return value_zer(a, b), None
        else:
            return None, None

print(solve_quadratic_equation(2,8,2))
print(solve_quadratic_equation(1,2,1))
print(solve_quadratic_equation(2,3,3))
