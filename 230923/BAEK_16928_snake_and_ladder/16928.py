from collections import deque

dice = [1, 2, 3, 4, 5, 6]


def bfs(start):
    dq = deque()
    dq.append(start)
    visited[start] = 1
    while dq:
        now = dq.popleft()
        for d in dice:
            next = now+d
            if 0<=next<101:
                if visited[next] < visited[now] + 1:
                    continue
                visited[next] = visited[now] + 1
                if board[next] != 0:
                    new_next = board[next]
                    if visited[new_next] > visited[next]:
                        visited[new_next] = visited[next]
                        dq.append(new_next)
                else:
                    dq.append(next)


N, M = map(int, input().split())
board = [0]*101
INF = int(1e9)
visited = [INF]*101
for _ in range(N+M):
    u, v = map(int, input().split())
    board[u] = v
bfs(1)
print(visited[100] - 1)
