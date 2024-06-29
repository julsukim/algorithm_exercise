from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(si, sj):
    pq = []
    heappush(pq, (0, si, sj))
    visited[si][sj] = 0
    while pq:
        dist, i, j = heappop(pq)

        if visited[i][j] < dist:
            continue

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N:
                next_dist = dist
                if arr[ni][nj] == 0:
                    next_dist = dist + 1
                if visited[ni][nj] <= next_dist:
                    continue
                visited[ni][nj] = next_dist
                heappush(pq, (next_dist, ni, nj))


N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
INF = float('inf')
visited = [[INF] * N for _ in range(N)]
dijkstra(0, 0)
print(visited[N-1][N-1])
