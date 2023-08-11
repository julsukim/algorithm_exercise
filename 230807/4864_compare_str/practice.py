import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str_1 = input()
    str_2 = input()
    M = len(str_1)
    N = len(str_2)

    result = 0
    for i in range(N-M+1):
        for j in range(M):
            if str_2[i+j] != str_1[j]:
                break
        else:
            result = 1

    print(f'#{tc} {result}')