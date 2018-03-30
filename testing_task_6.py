def is_str_isogramm (string):
    answer = False
    lit_number = -1
    while answer == False:
        lit_number += 1
        if not string.rfind(string[lit_number]) == lit_number - 1:
            return True
        else:
            return False





print(is_str_isogramm('goose'))