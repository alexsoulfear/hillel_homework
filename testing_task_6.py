def is_str_isogramm (string):
    answer = False
    for i in range(len(string)):
        if not (int(string.rfind(string[i]))) == i:
            answer = True
            break
    return print(answer)

is_str_isogramm('mergg')