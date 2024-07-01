import sys
sys.stdin = open('input.txt')


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
board = [input() for _ in range(N)]
vt = [[0]*M for _ in range(N)]
print(board)
loc_R = 0
loc_B = 0
loc_O = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '#' or board[i][j] == '.':
            continue
        elif board[i][j] == 'R':
            loc_R = [i, j]
        elif board[i][j] == 'B':
            loc_B = [i, j]
        elif board[i][j] == 'O':
            loc_O = [i, j]
print(loc_R, loc_B, loc_O)
