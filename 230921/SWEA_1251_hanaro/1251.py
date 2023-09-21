import sys, heapq, math
sys.stdin = open('input.txt')


def seek(start):
    heap = []
    heapq.heappush(heap, (0, start))
    sum_weight = 0
    while heap:
        w, v = heapq.heappop(heap)

        if visited[v]:
            continue

        visited[v] = 1
        sum_weight += w

        for k in range(N):
            if k == v:
                continue
            nw = E*(math.sqrt((abs(xs[v]-xs[k]))**2 + (abs(ys[v]-ys[k]))**2))**2
            if visited[k]:
                continue
            else:
                heapq.heappush(heap, (nw, k))
    return sum_weight



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())

    visited = [0]*N

    result = seek(0)
    print(f'#{tc} {round(result)}')
