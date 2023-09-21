import sys, heapq
sys.stdin = open('input.txt')


def prim(start):
    heap = []
    MST = [0]*(V+1)
    heapq.heappush(heap, (0, start))
    sum_weight = 0
    while heap:
        weight, v = heapq.heappop(heap)

        if MST[v]:
            continue

        MST[v] = 1
        sum_weight += weight

        for next in graph[v]:
            if MST[next[0]]:
                continue

            heapq.heappush(heap, (next[1], next[0]))

    return sum_weight


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append([n2, w])
        graph[n2].append([n1, w])

    result = prim(0)
    print(f'#{tc} {result}')
