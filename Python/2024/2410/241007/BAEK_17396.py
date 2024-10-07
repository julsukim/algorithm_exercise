import heapq, sys
input = sys.stdin.readline

N, M = map(int, input().split())
sight = list(map(int, input().rstrip().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])
    graph[b].append([a, t])

INF = sys.maxsize
distance = [INF] * N


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_dist = dist + cost

            if next_node != N-1:
                if sight[next_node] == 1:
                    continue

            if distance[next_node] <= new_dist:
                continue

            distance[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))


dijkstra(0)
if distance[N-1] == INF:
    print(-1)
else:
    print(distance[N-1])
