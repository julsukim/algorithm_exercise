from heapq import heappush, heappop


def dijkstra(start):
    i, j = start
    heapq = []
    heappush(heapq, (graph[i][j], start))
    costs[i][j] = graph[i][j]
    while heapq:
        cost, now = heappop(heapq)

        if costs[now[0]][now[1]] < cost:
            continue

        for d in delta:
            ni, nj = now[0]+d[0], now[1]+d[1]
            if 0<=ni<N and 0<=nj<N:
                new_cost = cost + graph[ni][nj]

                if costs[ni][nj] <= new_cost:
                    continue

                costs[ni][nj] = new_cost
                heappush(heapq, (new_cost, (ni, nj)))

    print(f'Problem {tc}: {costs[N-1][N-1]}')


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INF = int(1e9)
tc = 1

while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    costs = [[INF]*N for _ in range(N)]

    dijkstra((0, 0))
    tc += 1
