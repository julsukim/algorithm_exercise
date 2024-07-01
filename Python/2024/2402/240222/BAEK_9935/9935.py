import re

str_target = input()
str_bomb = input()


def explode(target):
    str_len = len(target)
    bomb = re.compile(str_bomb)
    result = bomb.search(target)
    if result is None:
        print(target)
        return
    else:
        start = result.span()[0]
        end = result.span()[1]
        if (start == 0) & (end == str_len):
            print('FRULA')
            return
        elif start == 0:
            explode(target[end:])
        elif end == str_len:
            explode(target[:start])
        else:
            str_1 = target[:start]
            str_2 = target[end:]
            explode(str_1 + str_2)


explode(str_target)
