import sys
sys.stdin = open('input.txt')

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    ground = [[0] * 9 for _ in range(9)]
    ground[N // 2][N // 2] = 2
    ground[N // 2][N // 2 + 1] = 1
    ground[N // 2 + 1][N // 2] = 1
    ground[N // 2 + 1][N // 2 + 1] = 2

    for _ in range(M):
        arr = list(map(int, input().split()))
        x, y, color = arr[1], arr[0], arr[2]
        ground[x][y] = color

        for k in range(8):
            for l in range(1, N):
                ni, nj = x + l*di[k], y + l*dj[k]
                if 0 <= ni < N+1 and 0 <= nj < N+1:
                    if ground[ni][nj] == 0:
                        break
                    elif ground[ni][nj] != color:
                        continue
                    elif ground[ni][nj] == color:
                        for p in range(1, l):
                            ci, cj = x + p*di[k], y + p*dj[k]
                            ground[ci][cj] = color
                        else:
                            break

    b_count = 0
    w_count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if ground[i][j] == 1:
                b_count += 1
            elif ground[i][j] == 2:
                w_count += 1

    print(f'#{tc} {b_count} {w_count}')