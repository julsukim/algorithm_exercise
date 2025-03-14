import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

maximum = 0

# 2*2
for i in range(n-1):
    for j in range(m-1):
        tmp = sum(board[i][j:j+2]) + sum(board[i+1][j:j+2])
        maximum = max(maximum, tmp)

# 1*4
for i in range(n):
    for j in range(m-3):
        tmp = sum(board[i][j:j+4])
        maximum = max(maximum, tmp)
# 4*1
for i in range(n-3):
    for j in range(m):
        tmp = sum([board[i + k][j] for k in range(4)])
        maximum = max(maximum, tmp)

for i in range(n-2):
    for j in range(m-1):
        # L 0
        tmp = sum([board[i + k][j] for k in range(3)] + [board[i+2][j+1]])
        # L 0 R
        tmp2 = sum([board[i + k][j+1] for k in range(3)] + [board[i+2][j]])
        # L 180
        tmp3 = sum([board[i + k][j+1] for k in range(3)] + [board[i][j]])
        # L 180 R
        tmp4 = sum([board[i + k][j] for k in range(3)] + [board[i][j+1]])
        maximum = max([maximum, tmp, tmp2, tmp3, tmp4])

for i in range(n-1):
    for j in range(m-2):
        # L 90
        tmp = sum(board[i][j:j+3] + [board[i+1][j]])
        # L 90 R
        tmp2 = sum(board[i][j:j+3] + [board[i+1][j+2]])
        # L 270
        tmp3 = sum(board[i+1][j:j + 3] + [board[i][j+2]])
        # L 270 R
        tmp4 = sum(board[i+1][j:j + 3] + [board[i][j]])
        maximum = max([maximum, tmp, tmp2, tmp3, tmp4])

for i in range(n-1):
    for j in range(m-2):
        # ㅜ
        tmp = sum(board[i][j:j+3] + [board[i+1][j+1]])
        # ㅜ 180 (ㅗ)
        tmp2 = sum(board[i+1][j:j+3] + [board[i][j+1]])
        maximum = max([maximum, tmp, tmp2])

for i in range(n-2):
    for j in range(m-1):
        # ㅜ 90 (ㅓ)
        tmp = sum([board[i+k][j+1] for k in range(3)] + [board[i+1][j]])
        # ㅜ 270 (ㅏ)
        tmp2 = sum([board[i + k][j] for k in range(3)] + [board[i + 1][j+1]])
        maximum = max([maximum, tmp, tmp2])

for i in range(n-2):
    for j in range(m-1):
        # 4
        tmp = sum([board[i][j], board[i+1][j], board[i+1][j+1], board[i+2][j+1]])
        # 4 0 R
        tmp2 = sum([board[i][j+1], board[i+1][j+1], board[i+1][j], board[i+2][j]])
        maximum = max([maximum, tmp, tmp2])

for i in range(n-1):
    for j in range(m-2):
        # 4 90
        tmp = sum([board[i+1][j], board[i+1][j+1], board[i][j+1], board[i][j+2]])
        # 4 90 R
        tmp2 = sum([board[i][j], board[i][j+1], board[i+1][j+1], board[i+1][j+2]])
        maximum = max([maximum, tmp, tmp2])

print(maximum)
