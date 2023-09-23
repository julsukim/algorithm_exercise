from collections import deque
import sys
input = sys.stdin.readline

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(start):
    dq = deque()
    br, p, q = start
    visited[br][p][q] = 1
    dq.append(start)
    while dq:
        breaked, cp, cq = dq.popleft()
        if cp == N-1 and cq == M-1:
            return visited[breaked][cp][cq]

        for d in delta:
            np, nq = cp+d[0], cq+d[1]

            if 0<=np<N and 0<=nq<M and visited[breaked][np][nq] == 0:
                if arr[np][nq] == 0:
                    visited[breaked][np][nq] = visited[breaked][cp][cq] + 1
                    dq.append((breaked, np, nq))
                if breaked == 0 and arr[np][nq] == 1:
                    new_breaked = 1
                    visited[new_breaked][np][nq] = visited[breaked][cp][cq] + 1
                    dq.append((new_breaked, np, nq))

    return -1


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[0]*M for _ in range(N)] for _ in range(2)]

# (벽부순지 여부, i좌표, j좌표)
print(bfs((0, 0, 0)))
