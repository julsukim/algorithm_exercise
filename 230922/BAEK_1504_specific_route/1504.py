from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(start):
    distance = [INF] * (N + 1)
    heapq = []
    heappush(heapq, (0, start))
    distance[start] = 0
    while heapq:
        dist, now = heappop(heapq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            next_dist = next[1]

            new_dist = dist + next_dist

            if distance[next_node] <= new_dist:
                continue

            distance[next_node] = new_dist
            heappush(heapq, (new_dist, next_node))
    return distance


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

INF = int(1e9)

start_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

case1 = start_dist[v1] + v1_dist[v2] + v2_dist[N]
case2 = start_dist[v2] + v2_dist[v1] + v1_dist[N]

result = min(case1, case2)
print(result if result < INF else -1)
