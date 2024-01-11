import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    str_1 = input()
    str_2 = input()

    str_e = ''
    for i in str_1:
        if i not in str_e:
            str_e += i
    N = len(str_e)

    str_count = {}
    for i in range(N):
        str_count[str_e[i]] = 0

    for i in str_2:
        for j in str_e:
            if i == j:
                str_count[j] += 1

    max_count = 0
    for i in str_count:
        if max_count < str_count[i]:
            max_count = str_count[i]

    print(f'#{tc} {max_count}')