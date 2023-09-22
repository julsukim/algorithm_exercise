from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start):
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
    return


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
INF = int(1e9)
distance = [INF]*(V+1)

dijkstra(K)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
        continue
    print(distance[i])
