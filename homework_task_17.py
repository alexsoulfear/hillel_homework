import math
def solve_quadratic_equation(a, b, c):
    descr = b ** 2 - 4 * a * c
    def values_pl (a, b):
        value_1 = (-b - math.sqrt(descr)) / a * 2
        value_2 = (-b - math.sqrt(descr)) / a * 2
        return value_1, value_2
    def value_zer (a, b):
        value = (-b - math.sqrt(descr)) / a * 2
        return value
    if descr > 0:
        return values_pl(a, b)
    else:
        if descr == 0:
            return value_zer(a, b)
        else:
            return "none"

print(solve_quadratic_equation(2,8,2))
print(solve_quadratic_equation(1,2,1))
print(solve_quadratic_equation(2,3,3))