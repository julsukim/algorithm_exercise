from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def prim(start):
    heap = []
    MST = [0]*(V+1)
    heappush(heap, (0, start))
    sum_weight = 0
    while heap:
        weight, now = heappop(heap)
        if MST[now]:
            continue
        MST[now] = 1
        sum_weight += weight
        for next in graph[now]:
            if MST[next[0]]:
                continue
            heappush(heap, (next[1], next[0]))
    return sum_weight


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

print(prim(1))
