import sys
sys.stdin = open('input.txt')


def ispalin(str):
    N = len(str)
    for i in range(N//2 + 1):
        if str[i] != str[N-i-1]:
            return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    word = input()
    result = ispalin(word)

    print(f'#{tc} {result}')