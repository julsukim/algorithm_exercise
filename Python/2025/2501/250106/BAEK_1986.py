import sys
input = sys.stdin.readline

n, m = map(int, input().split())
queens = 0
knights = 0
pawns = 0

# 0 Safe, 1 Danger, 2 Q, 3 K, 4 P
board = [[0] * m for _ in range(n)]

for time in range(3):
    input_arr = list(map(int, input().split()))

    if time == 0:
        queens = input_arr[0]
        for i in range(0, input_arr[0]):
            board[input_arr[2 * i + 1] - 1][input_arr[2 * i + 2] - 1] = 2
    elif time == 1:
        knights = input_arr[0]
        for i in range(0, input_arr[0]):
            board[input_arr[2 * i + 1] - 1][input_arr[2 * i + 2] - 1] = 3
    elif time == 2:
        pawns = input_arr[0]
        for i in range(0, input_arr[0]):
            board[input_arr[2 * i + 1] - 1][input_arr[2 * i + 2] - 1] = 4

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 or board[i][j] == 1:
            continue

        if board[i][j] == 2:
            for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                multi = 1
                while True:
                    ni, nj = i + (di*multi), j + (dj*multi)
                    if ni < 0 or nj < 0 or ni >= n or nj >= m:
                        break
                    if board[ni][nj] == 2 or board[ni][nj] == 3 or board[ni][nj] == 4:
                        break
                    board[ni][nj] = 1
                    multi += 1

        elif board[i][j] == 3:
            for di, dj in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] != 2 and board[ni][nj] != 3 and board[ni][nj] != 4:
                    board[ni][nj] = 1

print(sum(row.count(0) for row in board))
