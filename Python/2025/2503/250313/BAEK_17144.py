# 공기청정기는 항상 1번 열 (두 행을 차지)
# 1. 미세먼지 확산 (r, c)의 미세먼지는 인접한 네 방향으로 확산 (모든 칸에서 동시에 일어남)
#   - 인접한 방향에 공기청정기가 있거나 칸이 없으면 그 방향으로는 확산되지 않음
#   - 확산되는 양은 // 5
#   - 남은 양은 (r, c) - ((r, c) // 5 * 확산 수))
# 2. 공기청정기 작동
#   - 위쪽은 반시계방향
#   - 아래쪽은 시계방향
#   - 공기청정기로 들어간 미세먼지는 모두 정화
# T초가 지난 후 방의 미세먼지 양의 총합

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(R)]

a1 = a2 = -1

for i in range(R):
    if field[i][0] == -1:
        if a1 == -1:
            a1 = i
        elif a2 == -1:
            a2 = i

for _ in range(T):
    new_field = [[0]*C for _ in range(R)]
    new_field[a1][0] = new_field[a2][0] = -1

    for i in range(R):
        for j in range(C):
            if field[i][j] == 0 or field[i][j] == -1:
                continue
            spread_cnt = 0
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and field[ni][nj] != -1:
                    new_field[ni][nj] += field[i][j] // 5
                    spread_cnt += 1
            new_field[i][j] += field[i][j] - ((field[i][j] // 5) * spread_cnt)

    field = new_field

    previous = field[a1][1]
    for j in range(2, C):
        tmp = field[a1][j]
        field[a1][j] = previous
        previous = tmp

    for i in range(a1 - 1, -1, -1):
        tmp = field[i][C-1]
        field[i][C-1] = previous
        previous = tmp

    for j in range(C-2, -1, -1):
        tmp = field[0][j]
        field[0][j] = previous
        previous = tmp

    for i in range(1, a1 + 1):
        tmp = field[i][0]
        field[i][0] = previous
        previous = tmp

    field[a1][1] = 0
    field[a1][0] = -1

    previous = field[a2][1]
    for j in range(2, C):
        tmp = field[a2][j]
        field[a2][j] = previous
        previous = tmp

    for i in range(a2 + 1, R):
        tmp = field[i][C-1]
        field[i][C-1] = previous
        previous = tmp

    for j in range(C-2, -1, -1):
        tmp = field[R-1][j]
        field[R-1][j] = previous
        previous = tmp

    for i in range(R-2, a2-1, -1):
        tmp = field[i][0]
        field[i][0] = previous
        previous = tmp

    field[a2][1] = 0
    field[a2][0] = -1

print(sum([sum(row) for row in field]) + 2)
