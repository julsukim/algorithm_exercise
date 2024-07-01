from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            next_cost = next[1]

            new_cost = dist + next_cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heappush(pq, (new_cost, next_node))


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])
A, B = map(int, input().split())

INF = float('inf')
distance = [INF] * (N+1)

dijkstra(A)
print(distance[B])
