import heapq, sys
input = sys.stdin.readline


def dijkstra(graph, start, target_y):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return min([distances[node] for node in distances if node[1] == target_y], default=float('inf'))


n, f = map(int, input().split())
coords = [tuple(map(int, input().split())) for _ in range(n)]
coords.append((0, 0))  # 시작점 추가
graph = {}

for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        if abs(coords[i][0] - coords[j][0]) <= 2 and abs(coords[i][1] - coords[j][1]) <= 2:
            distance = ((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2) ** 0.5
            graph.setdefault(coords[i], {})[coords[j]] = distance
            graph.setdefault(coords[j], {})[coords[i]] = distance

shortest_distance = dijkstra(graph, (0, 0), f)
print(-1 if shortest_distance == float('inf') else round(shortest_distance))
