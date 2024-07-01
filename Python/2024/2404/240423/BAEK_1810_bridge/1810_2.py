import heapq, sys
input = sys.stdin.readline


def dijkstra(graph, start_index, target_y, coord_index_map):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start_index] = 0
    queue = [(0, start_index)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    # target_y에 해당하는 모든 좌표들의 인덱스 찾기
    target_indices = [index for coord, index in coord_index_map.items() if coord[1] == target_y]

    # target_indices에 해당하는 최단 거리 찾기
    return min([distances[i] for i in target_indices], default=float('inf'))


n, f = map(int, input().split())
coords = [tuple(map(int, input().split())) for _ in range(n)]
coords.append((0, 0))  # Add starting point

# 좌표를 인덱스로 매핑
coord_index_map = {coord: i for i, coord in enumerate(coords)}

graph = [[] for _ in range(len(coords))]

for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        if abs(coords[i][0] - coords[j][0]) <= 2 and abs(coords[i][1] - coords[j][1]) <= 2:
            distance = ((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2) ** 0.5
            graph[coord_index_map[coords[i]]].append((coord_index_map[coords[j]], distance))
            graph[coord_index_map[coords[j]]].append((coord_index_map[coords[i]], distance))

start_index = coord_index_map[(0, 0)]
shortest_distance = dijkstra(graph, start_index, f, coord_index_map)
print(-1 if shortest_distance == float('inf') else round(shortest_distance))
