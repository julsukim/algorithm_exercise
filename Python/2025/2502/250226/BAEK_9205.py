import sys
from collections import deque

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    coords = [tuple(map(int, input().split())) for _ in range(n + 2)]


    def manhattan(p, q):
        return abs(p[0] - q[0]) + abs(p[1] - q[1])


    # 각 지점들을 노드로 생각하여 그래프 구성
    graph = [[] for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(i + 1, n + 2):
            if manhattan(coords[i], coords[j]) <= 1000:
                graph[i].append(j)
                graph[j].append(i)

    # BFS 탐색: 집(노드 0)에서 시작하여 페스티벌(노드 n+1) 도달 여부 확인
    visited = [False] * (n + 2)
    queue = deque([0])
    visited[0] = True
    reachable = False
    while queue:
        cur = queue.popleft()
        if cur == n + 1:  # 페스티벌 도착
            reachable = True
            break
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    print("happy" if reachable else "sad")
