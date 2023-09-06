import sys
sys.stdin = open('input.txt')


def cla_d(arr):
    min_d = 0
    for j in range(H):
        p, q = homes[j]
        dis = 10000
        for k in range(M):
            p2, q2 = stores[arr[k]]
            if dis > abs(p - p2) + abs(q - q2):
                dis = abs(p - p2) + abs(q - q2)
        min_d += dis
    return min_d


def nCr(n, r, s):
    if r == 0:
        result.append(cla_d(subset))
    else:
        for i in range(s, n-r+1):
            subset[r-1] = arr[i]
            nCr(n, r-1, i+1)


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

H = len(homes)
S = len(stores)

result = []
arr = list(range(0, S))
subset = [0]*M

nCr(S, M, 0)

print(min(result))