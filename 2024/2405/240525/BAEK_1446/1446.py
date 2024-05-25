from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append([i+1, 1])

for _ in range(N):
    start, end, dist = map(int, input().split())
    if end > D:
        continue
    graph[start].append([end, dist])


def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cost, now = heappop(queue)

        if distance[now] < cost:
            continue

        for next in graph[now]:
            next_node = next[0]
            next_dist = next[1]
            new_dist = cost + next_dist

            if distance[next_node] <= new_dist:
                continue

            distance[next_node] = new_dist
            heappush(queue, (new_dist, next_node))


INF = int(1e9)
distance = [INF] * (D + 1)
dijkstra(0)
print(distance[D])
