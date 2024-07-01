from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def prim(start):
    heap = []
    MST = [0]*(N+1)
    heappush(heap, start)
    sum_move = 0
    while heap:
        now = heappop(heap)
        if MST[now] == 1:
            continue
        MST[now] = 1
        sum_move += 1
        for next in graph[now]:
            if MST[next] == 1:
                continue
            heappush(heap, next)
    return sum_move


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(prim(1) - 1)
