import sys
sys.stdin = open('input.txt')


def find_loss(arr):
    s = 0
    for i in range(len(arr)-1):
        s += loss[arr[i]-1][arr[i+1]-1]
    return s


def search_course(i, N):
    global min_loss
    if i == N:
        a = find_loss(p)
        if min_loss > a:
            min_loss = a
            return
        return
    else:
        for j in range(0, N):
            if used[j] == 0:
                p[i] = area[j]
                used[j] = 1
                search_course(i+1, N)
                used[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    loss = [list(map(int, input().split())) for _ in range(N)]

    min_loss = 50000
    area = list(range(1, N+1)) + [1]
    used = [1]+[0] * (N+1)
    p = [1] + [0] * (N-1) + [1]
    search_course(1, N)
    print(f'#{tc} {min_loss}')
