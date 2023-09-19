from collections import deque
import sys
input = sys.stdin.readline


def bfs(r):
    global cnt
    deque.append(r)
    visited[r] = cnt
    while len(deque) != 0:
        t = deque.popleft()
        for w in arr[t]:
            if visited[w] == 0:
                deque.append(w)
                cnt += 1
                visited[w] = cnt

    return


N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

for row in arr:
    row.sort(reverse=True)

cnt = 1
visited = [0] * (N+1)
deque = deque()
bfs(R)

for i in range(1, N+1):
    print(visited[i])