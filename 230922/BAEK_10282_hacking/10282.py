from heapq import heappop, heappush
import sys

input = sys.stdin.readline


def dijkstra(start):
    heapq = []
    heappush(heapq, (0, start))
    times[start] = 0
    while heapq:
        t, now = heappop(heapq)

        if times[now] < t:
            continue

        for next in graph[now]:
            n_n = next[0]
            n_t = next[1]

            t_t = t + n_t
            if times[n_n] <= t_t:
                continue

            times[n_n] = t_t
            heappush(heapq, (t_t, n_n))

    return


T = int(input())
for tc in range(1, T+1):
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(D):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    INF = int(1e9)
    times = [INF]*(N+1)

    dijkstra(C)
    count = 0
    for i in range(N+1):
        if times[i] == INF:
            times[i] = 0
            continue
        count += 1

    print(count, max(times))
