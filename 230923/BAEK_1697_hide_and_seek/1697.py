from collections import deque


def bfs(start):
    visited[start] = 1
    dq = deque()
    dq.append(start)
    while dq:
        if visited[K] != 0:
            break
        now = dq.popleft()
        if now == K:
            break
        for next in [now+1, now-1, now*2]:
            if 0<=next<200001 and visited[next] == 0:
                visited[next] = visited[now]+1
                dq.append(next)
    return visited[K]


N, K = map(int, input().split())
arr = [0]*200001
visited = [0]*200001

print(bfs(N) - 1)
