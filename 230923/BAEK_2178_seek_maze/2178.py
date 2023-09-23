from collections import deque
import sys
input = sys.stdin.readline

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs (start):
    p, q = start
    dq = deque()
    dq.append(start)
    visited[p][q] = 1
    while dq:
        cp, cq = dq.popleft()
        for d in delta:
            np, nq = cp+d[0], cq+d[1]
            if 0<=np<N and 0<=nq<M:
                if maze[np][nq] == 0 or visited[np][nq] != 0:
                    continue
                visited[np][nq] = visited[cp][cq] + 1
                dq.append((np, nq))

    return visited[N-1][M-1]


N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

result = bfs((0, 0))
print(result)
