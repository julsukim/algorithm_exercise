from heapq import heappop, heappush

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append([e, cost])
    graph[e].append([s, cost])

INF = int(1e9)
distance = [INF] * (N+1)


def dijkstra(start):
    pq = []

    heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        cost, now = heappop(pq)

        if distance[now] < cost:
            continue

        for next in graph[now]:
            next_node = next[0]
            next_cost = next[1]

            new_cost = cost + next_cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heappush(pq, (new_cost, next_node))


dijkstra(1)
print(distance[N])
