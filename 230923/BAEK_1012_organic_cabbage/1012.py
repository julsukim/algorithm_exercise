from collections import deque
import sys
input = sys.stdin.readline

delta = [(-1, 0), (0, 1), (0, -1), (1, 0)]


def bfs(start):
    p, q = start
    dq = deque()
    dq.append(start)
    visited[p][q] = 1
    while dq:
        cp, cq = dq.popleft()
        for d in delta:
            np, nq = cp+d[0], cq+d[1]
            if 0<=np<N and 0<=nq<M:
                if ground[np][nq] == 0 or visited[np][nq] == 1:
                    continue
                dq.append((np, nq))
                visited[np][nq] = 1
    return


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1

    visited = [[0]*M for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 0 or visited[i][j] == 1:
                continue
            bfs((i, j))
            count += 1

    print(count)
