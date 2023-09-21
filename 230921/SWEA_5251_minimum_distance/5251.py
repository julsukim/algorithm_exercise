import sys, heapq
sys.stdin = open('input.txt')


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dis, now = heapq.heappop(heap)

        if distance[now] < dis:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            if distance[next_node] <= dis + cost:
                continue
            else:
                distance[next_node] = dis + cost
                heapq.heappush(heap, (dis + cost, next_node))

    return distance


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    INF = int(1e9)
    distance = [INF] * (N+1)

    result = dijkstra(0)
    print(f'#{tc} {result[N]}')
