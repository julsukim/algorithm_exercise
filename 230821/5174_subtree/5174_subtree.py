import sys
sys.stdin = open('input.txt')


def preorder(n):
    global count
    if n:
        count += 1
        preorder(child_1[n])
        preorder(child_2[n])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    child_1 = [0] * (E+2)
    child_2 = [0] * (E+2)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if child_1[p] == 0:
            child_1[p] = c
        else:
            child_2[p] = c

    count = 0
    preorder(N)
    print(f'#{tc} {count}')
