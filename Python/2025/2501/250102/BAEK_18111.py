import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

best_time = float('inf')
best_height = 0

for floor in range(257):
    tmp_time = 0
    block = B
    for i in range(N):
        for j in range(M):
            if ground[i][j] <= floor:
                tmp_time += floor - ground[i][j]
                block -= floor - ground[i][j]
            else:
                tmp_time += 2 * (ground[i][j] - floor)
                block += ground[i][j] - floor
    if block >= 0:
        if tmp_time < best_time:
            best_time = tmp_time
            best_height = floor
        elif tmp_time == best_time and floor > best_height:
            best_height = floor

print(best_time, best_height)
