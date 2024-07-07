from collections import deque
import sys
input = sys.stdin.readline


def bfs(node, visited, sec, is_weak):
    i, j = node
    queue = deque([(i, j)])
    visited[i][j] = sec

    if is_weak:
        while queue:
            pi, pj = queue.popleft()
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = pi + di, pj + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if not arr[pi][pj] == 'B':
                        if not arr[ni][nj] == 'B':
                            if visited[ni][nj] == 0:
                                visited[ni][nj] = sec
                                queue.append((ni, nj))
                    else:
                        if arr[pi][pj] == arr[ni][nj]:
                            if visited[ni][nj] == 0:
                                visited[ni][nj] = sec
                                queue.append((ni, nj))
    else:
        while queue:
            pi, pj = queue.popleft()
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = pi + di, pj + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[pi][pj] == arr[ni][nj]:
                        if visited[ni][nj] == 0:
                            visited[ni][nj] = sec
                            queue.append((ni, nj))
    return


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

visited_a = [[0]*N for _ in range(N)]
visited_b = [[0]*N for _ in range(N)]

a = 0
b = 0

for i in range(N):
    for j in range(N):
        if visited_a[i][j] == 0:
            a += 1
            bfs((i, j), visited_a, a, False)
        if visited_b[i][j] == 0:
            b += 1
            bfs((i, j), visited_b, b, True)

print(a, b)
