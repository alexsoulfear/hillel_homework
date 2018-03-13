def have_trains_crashed(v1, v2):
    if v1 / 4 > v2 / 6:
        return False
    else:
        return True
print(have_trains_crashed(4,5))
print(have_trains_crashed(4,6))
print(have_trains_crashed(4,7))