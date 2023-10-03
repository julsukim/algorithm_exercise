import sys
sys.stdin = open('input.txt')

# 상, 하, 좌, 우 : 1, 2, 3, 4
delta = {1: (-1, 0),
         2: (1, 0),
         3: (0, -1),
         4: (0, 1)}
reverse = {1: 2,
           2: 1,
           3: 4,
           4: 3}

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    micro = [list(map(int, input().split())) for _ in range(K)]
    # 약품처리 : 0, N-1

    time = 0
    while time < M:
        time += 1
        for m in micro:
            m[0] += delta[m[3]][0]
            m[1] += delta[m[3]][1]

        coord = {}
        for m in micro:
            try:
                coord[(m[0], m[1])].append(m)
            except KeyError:
                coord[(m[0], m[1])] = [m]

        micro = []
        for c in coord:
            if c[0] == 0 or c[0] == N-1 or c[1] == 0 or c[1] == N-1:
                coord[c][0][2] //= 2
                coord[c][0][3] = reverse[coord[c][0][3]]
                if coord[c][0][2] != 0:
                    micro.append(coord[c][0])
            elif len(coord[c]) >= 2:
                nc = [coord[c][0][0], coord[c][0][1], 0, 0]
                largest = 0
                for i in coord[c]:
                    if largest < i[2]:
                        largest = i[2]
                        nc[3] = i[3]
                    nc[2] += i[2]
                micro.append(nc)
            else:
                micro.append(coord[c][0])

    rest = 0
    if len(micro) > 0:
        for i in range(len(micro)):
            rest += micro[i][2]

    print(f'#{tc} {rest}')
