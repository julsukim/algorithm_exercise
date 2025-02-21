from collections import deque
import sys
input = sys.stdin.readline

result = []

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                queue = deque([(i, j)])
                while queue:
                    ci, cj = queue.popleft()

                    if visited[ci][cj] == 1:
                        continue

                    visited[ci][cj] = 1
                    for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < h and 0 <= nj < w:
                            if graph[ni][nj] == 1:
                                queue.append((ni, nj))

    result.append(str(cnt))

print('\n'.join(result))
