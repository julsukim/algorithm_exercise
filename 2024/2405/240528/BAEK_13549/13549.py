from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
INF = int(1e9)


def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    distance = [INF] * 100001
    distance[start] = 0

    while queue:
        dist, now = heappop(queue)

        if distance[now] < dist:
            continue

        for next in [now+1, now-1, now*2]:
            if 0 <= next <= 100000:
                if next == now*2 and distance[next] > dist:
                    distance[next] = dist
                    heappush(queue, (dist, next))
                elif distance[next] > dist:
                    distance[next] = dist + 1
                    heappush(queue, (dist + 1, next))

    return distance


if K <= N:
    print(N-K)
else:
    result = dijkstra(N)
    print(result[K])
