import math

def triangle_square_and_perimeter(a, b):
    tri_sq = ((a * b)/ 2)
    tri_per = (a + b + (math.sqrt((a**2) + (b**2))))
    return tri_per, tri_sq

print(triangle_square_and_perimeter(5, 5))
