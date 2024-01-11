from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt')


N, M, K, X = map(int, input().split())

adj_arr = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int, input().split())
    adj_arr[start].append([1, end])

INF = int(1e9)
distance = [INF]*(N+1)


def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:
            continue

        for next in adj_arr[now]:
            next_node = next[1]
            cost = next[0]

            new_cost = dist + cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heappush(pq, (new_cost, next_node))


dijkstra(X)

is_find = False
for k in range(1, N+1):
    if distance[k] == K:
        print(k)
        is_find = True

if not is_find:
    print(-1)
