from heapq import heappush, heappop


def dijkstra(start, end, distance):
    heapq = []
    heappush(heapq, (0, start))
    distance[start] = 0
    while heapq:
        dist, now = heappop(heapq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heappush(heapq, (new_cost, next_node))

    return distance[end]


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    S, E, T = map(int, input().split())
    graph[S].append((E, T))
INF = int(1e9)
result = [0] * (N+1)

for i in range(1, N+1):
    distance1 = [INF] * (N + 1)
    distance2 = [INF] * (N + 1)
    r1 = dijkstra(i, X, distance1)
    r2 = dijkstra(X, i, distance2)
    result[i] = r1 + r2

print(max(result))
