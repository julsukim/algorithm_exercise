import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
field = [list(input().strip()) for _ in range(R)]
bomb_time = [[-1] * C for _ in range(R)]

# 초기 폭탄 설치 시간 설정 (t=0)
for i in range(R):
    for j in range(C):
        if field[i][j] == 'O':
            bomb_time[i][j] = 0

def in_range(i, j):
    return 0 <= i < R and 0 <= j < C

def plant_bombs(t):
    for i in range(R):
        for j in range(C):
            if field[i][j] == '.':
                field[i][j] = 'O'
                bomb_time[i][j] = t

def explode(t):
    # t-3초에 설치된 폭탄이 폭발함
    to_explode = []
    for i in range(R):
        for j in range(C):
            if bomb_time[i][j] == t - 3:
                to_explode.append((i, j))
    explode_positions = []
    for i, j in to_explode:
        explode_positions.append((i, j))
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if in_range(ni, nj):
                explode_positions.append((ni, nj))
    for i, j in set(explode_positions):
        field[i][j] = '.'
        bomb_time[i][j] = -1

if N == 1:
    # t=1일 때 초기 상태 그대로 출력
    for row in field:
        print(''.join(row))
else:
    # t=2부터 시뮬레이션 시작
    for t in range(2, N + 1):
        if t % 2 == 0:
            # 짝수 초: 빈 칸에 폭탄 설치
            plant_bombs(t)
        else:
            # 홀수 초: t-3초에 설치된 폭탄 폭발
            explode(t)
    for row in field:
        print(''.join(row))
