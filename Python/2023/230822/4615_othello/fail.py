import sys
sys.stdin = open('input.txt')

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    ground = [[0] * 9 for _ in range(9)]
    ground[N//2][N//2] = 'w'
    ground[N//2][N//2+1] = 'b'
    ground[N//2+1][N//2] = 'b'
    ground[N//2+1][N//2+1] = 'w'

    for _ in range(M):
        arr = list(map(int, input().split()))
        if arr[2] == 1:
            col = 'b'
        else:
            col = 'w'
        ground[arr[1]][arr[0]] = col
        for k in range(8):
            find = False
            for l in range(1, N):
                ni, nj = arr[1] + l * di[k], arr[0] + l * dj[k]
                if 0<=ni<(N+1) and 0<=nj<(N+1):
                    if ground[ni][nj] == 0:
                        break
                    elif ground[ni][nj] != col:
                        find = True
                        continue
                    if ground[ni][nj] == col and find == True:
                        for i in range(l-1, 0, -1):
                            ci, cj = arr[1] + i * di[k], arr[0] + i * dj[k]
                            ground[ci][cj] = col
                        break
                else:
                    break

    b_count = 0
    w_count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if ground[i][j] == 'b':
                b_count += 1
            elif ground[i][j] == 'w':
                w_count += 1

    print(f'#{tc} {b_count} {w_count}')