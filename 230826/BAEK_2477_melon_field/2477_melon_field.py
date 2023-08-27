import sys
sys.stdin = open('input.txt')

field = {
    1: [],
    2: [],
    3: [],
    4: []
}
info = []
N = int(input())
for _ in range(6):
    direction, length = map(int, input().split())
    field[direction].append(length)
    info.append((direction, length))

info = info * 3
short = {}
if len(field[1]) == 2 and len(field[3]) == 2:
    for i in range(len(info)-1):
        if info[i][0] == 2:
            short[3] = info[i + 1][1]
        elif info[i][0] == 4:
            short[1] = info[i - 1][1]
    result = (field[2][0] * short[3]) + (field[4][0] * short[1]) - (short[1] * short[3])

elif len(field[2]) == 2 and len(field[3]) == 2:
    for i in range(len(info) - 1):
        if info[i][0] == 4:
            short[2] = info[i + 1][1]
        elif info[i][0] == 1:
            short[3] = info[i - 1][1]
    result = (field[4][0] * short[2]) + (field[1][0] * short[3]) - (short[2] * short[3])

elif len(field[1]) == 2 and len(field[4]) == 2:
    for i in range(len(info) - 1):
        if info[i][0] == 3:
            short[1] = info[i + 1][1]
        elif info[i][0] == 2:
            short[4] = info[i - 1][1]
    result = (field[2][0] * short[4]) + (field[3][0] * short[1]) - (short[4] * short[1])

elif len(field[2]) == 2 and len(field[4]) == 2:
    for i in range(len(info) - 1):
        if info[i][0] == 1:
            short[4] = info[i + 1][1]
        elif info[i][0] == 3:
            short[2] = info[i - 1][1]
    result = (field[3][0] * short[2]) + (field[1][0] * short[4]) - (short[2] * short[4])

print(result*N)
