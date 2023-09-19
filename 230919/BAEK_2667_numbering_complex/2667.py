from collections import deque


def bfs(loc):
    c_cnt = 1
    i, j = loc
    dq.append(loc)
    visited[i][j] = 1
    while len(dq) > 0:
        i, j = dq.popleft()
        for k in range(4):
            ni, nj = i+delta[k][0], j+delta[k][1]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    dq.append((ni, nj))
                    visited[ni][nj] = 1
                    c_cnt += 1
    return c_cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [[0]*N for _ in range(N)]
dq = deque()

v_cnt = []
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            v_cnt.append(bfs((i, j)))
            cnt += 1
v_cnt.sort()
print(cnt)
for p in v_cnt:
    print(p)
