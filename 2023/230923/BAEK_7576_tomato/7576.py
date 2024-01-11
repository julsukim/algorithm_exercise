from collections import deque
import sys
input = sys.stdin.readline

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

dq = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            dq.append((i, j))

while dq:
    cp, cq = dq.popleft()
    for d in delta:
        np, nq = cp + d[0], cq + d[1]
        if 0 <= np < N and 0 <= nq < M:
            if box[np][nq] != 0:
                continue
            box[np][nq] = box[cp][cq] + 1
            dq.append((np, nq))

nono = False
maximum = 0

for p in range(N):
    for q in range(M):
        if box[p][q] == 0:
            nono = True
        elif maximum < box[p][q]:
            maximum = box[p][q]

print(maximum-1 if nono == False else -1)
