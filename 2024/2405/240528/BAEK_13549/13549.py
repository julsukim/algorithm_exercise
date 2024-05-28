from heapq import heappop, heappush

N, K = map(int, input().split())

INF = int(1e9)
limit = K*2 + 1


def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    distance = [INF] * limit
    distance[start] = 0

    while queue:
        dist, now = heappop(queue)

        if distance[now] < dist:
            continue

        for move in [-1, +1]:
            next_node = now + move

            if next_node < 0 or next_node >= limit:
                continue

            new_dist = dist + 1
            if distance[next_node] <= new_dist:
                continue

            heappush(queue, (new_dist, next_node))

        next_node = now * 2
        if next_node < 0 or next_node >= limit:
            continue
        new_dist = dist
        if distance[next_node] <= new_dist:
            continue
        heappush(queue, (new_dist, next_node))

    return distance


result = dijkstra(N)
print(result[K])
