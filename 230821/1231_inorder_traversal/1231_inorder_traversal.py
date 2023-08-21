import sys
sys.stdin = open('input.txt')


def inorder(n):
    if n:
        inorder(ch1[n])
        print(char[n], end='')
        inorder(ch2[n])


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    char = [0] * (N+1)

    for i in range(N):
        try:
            p = int(arr[i][0])
            w = arr[i][1]
            char[p] = w
            c1 = int(arr[i][2])
            ch1[p] = c1
            c2 = int(arr[i][3])
            ch2[p] = c2
        except IndexError:
            pass

    print(f'#{tc}', end=' ')
    inorder(1)
    print()