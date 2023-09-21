import sys, heapq
sys.stdin = open('input.txt')

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def seek(start):
    heap = []
    heapq.heappush(heap, (0, start))
    sp, sq = start
    visited[sp][sq] = 0
    while heap:
        w, v = heapq.heappop(heap)

        if visited[v[0]][v[1]] < w:
            continue

        for k in range(4):
            np, nq = v[0]+delta[k][0], v[1]+delta[k][1]
            if 0<=np<N and 0<=nq<N:
                add = 1
                if area[v[0]][v[1]] < area[np][nq]:
                    add += area[np][nq] - area[v[0]][v[1]]

                if visited[np][nq] <= w + add:
                    continue
                else:
                    visited[np][nq] = w + add
                    heapq.heappush(heap, (w + add, (np, nq)))
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int,input().split())) for _ in range(N)]
    INF = int(1e9)
    visited = [[INF]*N for _ in range(N)]

    seek((0, 0))
    print(f'#{tc} {visited[N-1][N-1]}')
