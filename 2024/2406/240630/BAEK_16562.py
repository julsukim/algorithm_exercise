from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
costs = [0] + list(map(int, input().split()))
relationships = list([] for _ in range(N+1))
for _ in range(M):
    v, w = map(int, input().split())
    relationships[v].append(w)
    relationships[w].append(v)

visited = [0] * (N+1)
queue = deque()
ans = 0

for i in range(1, N+1):
    if visited[i] == 0:
        queue.append(i)
        visited[i] = 1
        min_cost = costs[i]
        while queue:
            v = queue.popleft()
            for w in relationships[v]:
                if visited[w] == 0:
                    visited[w] = 1
                    queue.append(w)
                    min_cost = min(min_cost, costs[w])
        ans += min_cost

if ans <= K:
    print(ans)
else:
    print("Oh no")
