import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    TC = int(input())
    N = 100
    ladder_list = [list(map(int, input().split())) for _ in range(N)]

    key = 2
    for j in range(N):
        if ladder_list[-1][j] == key:
            aj = j
            ai = N-1

    di = [0, 0, -1]
    dj = [-1, 1, 0]

    X = 0

    loc = ladder_list[ai][aj]
    while ai != 0:
        for k in range(3):
            ladder_list[ai][aj] = 0
            ni, nj = ai+di[k], aj+dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if ladder_list[ni][nj] == 1:
                    ai = ni
                    aj = nj
                    continue

    print(f'#{TC} {aj}')
