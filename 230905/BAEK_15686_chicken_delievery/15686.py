import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    homes = []
    stores = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                homes.append((i, j))
            elif city[i][j] == 2:
                stores.append((i, j))

    chi_dis = []

    for i in range(len(stores)):
        r1, c1 = stores[i]
        dis = 0
        for j in range(len(homes)):
            r2, c2 = homes[j]
            dis += abs(r1 - r2) + abs(c1 - c2)
        chi_dis.append((i, dis))

    chi_dis.sort(key=lambda x:x[1])

    min_min_chi = 0
    for i in range(len(homes)):
        p3, q3 = homes[i]
        min_chi = 10000
        for j in range(M):
            p4, q4 = stores[chi_dis[j][0]]
            mini = abs(p3 - p4) + abs(q3 - q4)
            if min_chi > mini:
                min_chi = mini
        min_min_chi += min_chi

    print(min_min_chi)