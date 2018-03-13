import math
def circles_intersect(x1, y1, r1, x2, y2, r2):
    if math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) < r1 + r2:
        return True
    else:
        return False

print(circles_intersect(3,3,2,1,1,2))
print(circles_intersect(4,8,3,1,1,2))