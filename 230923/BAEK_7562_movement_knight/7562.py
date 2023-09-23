from collections import deque

delta = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]


def bfs(start):
    p, q = start
    dq = deque()
    dq.append(start)
    visited[p][q] = 1
    while dq:
        if visited[ti][tj] != 0:
            break
        cp, cq = dq.popleft()
        for d in delta:
            np, nq = cp+d[0], cq+d[1]
            if 0<=np<I and 0<=nq<I:
                if visited[np][nq] == 0:
                    visited[np][nq] = visited[cp][cq] + 1
                    dq.append((np, nq))
    return visited[ti][tj]


T = int(input())
for _ in range(T):
    I = int(input())
    si, sj = map(int, input().split())
    ti, tj = map(int, input().split())

    visited = [[0]*I for _ in range(I)]

    print(bfs((si, sj)) - 1)
