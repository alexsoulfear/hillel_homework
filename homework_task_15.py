import math
def circles_intersect(x1, y1, r1, x2, y2, r2):
    vector = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if vector > r1 + r2 \
            or vector + r1 < r2 \
            or vector + r2 < r1:
        return False
    if x1 == x2 and y1 == y2 and r1 == r2\
            or vector == r1 + r2:
        return True
    else:
        return True
# Тупо и в лоб!!!
print(circles_intersect(0, 0, 5, 0, 0, 4))