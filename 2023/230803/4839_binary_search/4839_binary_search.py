import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    BOOK = [*range(1, P+1, 1)]
    start = 1
    end = P
    count_a = 0
    count_b = 0
    while start <= end:
        count_a += 1
        middle = int((start + end)/2)
        if BOOK[middle-1] == Pa:
            break
        elif BOOK[middle-1] > Pa:
            end = middle - 1
        else:
            start = middle + 1

    start = 1
    end = P
    while start <= end:
        count_b += 1
        middle = (start + end)//2
        if BOOK[middle-1] == Pb:
            break
        elif BOOK[middle-1] > Pb:
            end = middle - 1
        else:
            start = middle + 1
    if count_a < count_b:
        win = 'A'
    elif count_a == count_b:
        win = 0
    else:
        win = 'B'

    print(f'#{tc} {win}')