from collections import deque

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
delta2 = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

queue = deque()

total = 0
visited = [[[-1] * W for _ in range(H)] for _ in range(K+1)]

queue.append([0, 0, 0])
flag = False

while queue:
    i, j, jump = queue.popleft()

    if i == H-1 and j == W-1:
        print(visited[jump][i][j] + 1)
        flag = True
        break

    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and visited[jump][ni][nj] == -1 and graph[ni][nj] != 1:
            visited[jump][ni][nj] = visited[jump][i][j] + 1
            queue.append([ni, nj, jump])

    if jump < K:
        for di, dj in delta2:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and visited[jump + 1][ni][nj] == -1 and graph[ni][nj] != 1:
                visited[jump + 1][ni][nj] = visited[jump][i][j] + 1
                queue.append([ni, nj, jump + 1])
if not flag:
    print(-1)
