import sys
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    a, *a_list = map(int, input().split())
    b, *b_list = map(int, input().split())

    result = 0
    if a_list.count(4) > b_list. count(4):
        result = 'A'
    elif a_list.count(4) < b_list. count(4):
        result = 'B'
    else:
        if a_list.count(3) > b_list.count(3):
            result = 'A'
        elif a_list.count(3) < b_list.count(3):
            result = 'B'
        else:
            if a_list.count(2) > b_list.count(2):
                result = 'A'
            elif a_list.count(2) < b_list.count(2):
                result = 'B'
            else:
                if a_list.count(1) > b_list.count(1):
                    result = 'A'
                elif a_list.count(1) < b_list.count(1):
                    result = 'B'
                else:
                    result = 'D'

    print(result)