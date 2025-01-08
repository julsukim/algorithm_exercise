# N : 0, S : 1, 12시 방향부터 시계 방향 순서
# [0] : 12시, [2] : 3시, [6] : 6시
# A, B, C, D
gears = [list(map(int, input())) for _ in range(4)]
K = int(input())

# 각 톱니바퀴의 12시 방향 인덱스
ai = 0 # +2
bi = 0 # +2, +6
ci = 0 # +2, +6
di = 0 # +6
# 회전 바퀴 번호, 방향 1 : 시계 방향, -1 : 반시계 방향
# 맞닿은 부분 극이 다르면 회전 방향과 반대 방향으로 회전
# 맞닿은 부분 극이 같으면 회전하지 않음


def rotate(index, direction):
    if direction == 0:
        return index
    elif direction == 1:
        return (index + 7) % 8
    elif direction == -1:
        return (index + 1) % 8


for i in range(K):
    order = list(map(int, input().split()))
    compare = [
        gears[0][(ai + 2) % 8] == gears[1][(bi + 6) % 8],
        gears[1][(bi + 2) % 8] == gears[2][(ci + 6) % 8],
        gears[2][(ci + 2) % 8] == gears[3][(di + 6) % 8]
    ]
    dir = order[1]
    rotation = [0] * 4
    if order[0] == 1:
        rotation[0] = dir
        if not compare[0]:
            rotation[1] = -dir
            if not compare[1]:
                rotation[2] = dir
                if not compare[2]:
                    rotation[3] = -dir
    elif order[0] == 2:
        rotation[1] = dir
        if not compare[0]:
            rotation[0] = -dir
        if not compare[1]:
            rotation[2] = -dir
            if not compare[2]:
                rotation[3] = dir
    elif order[0] == 3:
        rotation[2] = dir
        if not compare[2]:
            rotation[3] = -dir
        if not compare[1]:
            rotation[1] = -dir
            if not compare[0]:
                rotation[0] = dir
    elif order[0] == 4:
        rotation[3] = dir
        if not compare[2]:
            rotation[2] = -dir
            if not compare[1]:
                rotation[1] = dir
                if not compare[0]:
                    rotation[0] = -dir
    ai = rotate(ai, rotation[0])
    bi = rotate(bi, rotation[1])
    ci = rotate(ci, rotation[2])
    di = rotate(di, rotation[3])

score = 0
if gears[0][ai] == 1:
    score += 1
if gears[1][bi] == 1:
    score += 2
if gears[2][ci] == 1:
    score += 4
if gears[3][di] == 1:
    score += 8

print(score)
