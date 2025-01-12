import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cloud_points = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):
    delta = [0, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    di, si = map(int, input().split())
    tmp = set()
    for i, j in cloud_points:
        ni, nj = (i + (delta[di][0] * si) + N) % N, (j + (delta[di][1] * si) + N) % N
        board[ni][nj] += 1
        tmp.add((ni, nj))
    for i, j in tmp:
        for dr, dc in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            ni, nj = i + dr, j + dc
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] > 0:
                board[i][j] += 1
    tmp2 = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i, j) not in tmp:
                board[i][j] -= 2
                tmp2.append((i, j))
    cloud_points = tmp2

print(sum(sum(row) for row in board))
