from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * (N + 1)
parent = [-1] * (N + 1)
queue = deque()
queue.append(1)
visited[1] = 1
cycle = []
is_find = False
while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        if visited[neighbor] == -1:
            visited[neighbor] = visited[node] + 1
            parent[neighbor] = node
            queue.append(neighbor)
        elif parent[node] != neighbor and not is_find:
            is_find = True
            n1 = node
            path_1 = []
            while n1 != -1:
                path_1.append(n1)
                n1 = parent[n1]

            n2 = neighbor
            path_2 = []
            while n2 != -1:
                path_2.append(n2)
                n2 = parent[n2]

            path_2_set = set(path_2)
            ps1 = 0
            ps2 = 0
            for i, e in enumerate(path_1):
                if e in path_2_set:
                    ps2 = path_2.index(e)
                    ps1 = i
                    break

            cycle = path_1[:ps1+1] + path_2[:ps2+1]


cycle = set(cycle)

result = [0] * N
for i in range(1, N+1):
    if i in cycle:
        result[i-1] = 0
    else:
        q2 = deque()
        q2.append(i)
        visited2 = [-1] * (N + 1)
        visited2[i] = 0
        while q2:
            n = q2.popleft()
            if n in cycle:
                result[i-1] = visited2[n]
                break

            for neighbor in graph[n]:
                if visited2[neighbor] == -1:
                    visited2[neighbor] = visited2[n] + 1
                    q2.append(neighbor)
print(*result)
