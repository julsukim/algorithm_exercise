from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
adj_arr = [[] for _ in range(N+1)]
for c in arr:
    adj_arr[c[0]].append(c[1])
    adj_arr[c[1]].append(c[0])

t_visited = [0]*(N+1)
dq = deque()
count = set()
for i in range(1, N+1):
    if t_visited[i] == 0:
        t_visited[i] = 1
        visited = [0]*(N+1)
        visited[i] = 1
        dq.append(i)
        while dq:
            u = dq.popleft()
            for v in adj_arr[u]:
                if visited[v] == 0:
                    visited[v] = 1
                    t_visited[v] = 1
                    dq.append(v)
        count.add(tuple(visited))

print(len(count))
