from collections import deque
import sys
input = sys.stdin.readline


def dfs(s):
    print(s, end=' ')
    d_visited[s] = 1
    for w in arr[s]:
        if d_visited[w] == 0:
            d_visited[w] = 1
            dfs(w)


def bfs(s):
    deque.append(s)
    b_visited[s] = 1
    while len(deque) > 0:
        t = deque.popleft()
        print(t, end=' ')
        for w in arr[t]:
            if b_visited[w] == 0:
                deque.append(w)
                b_visited[w] = 1


N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

for row in arr:
    row.sort()

d_visited = [0]*(N+1)
b_visited = [0]*(N+1)
deque = deque()
dfs(V)
print()
bfs(V)
