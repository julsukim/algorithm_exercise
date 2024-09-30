from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while swan_queue:
        i, j = swan_queue.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < R and 0 <= nj < C:
                if graph[ni][nj] == '.' and not visited[ni][nj]:
                    swan_queue.append((ni, nj))
                    visited[ni][nj] = True
                elif graph[ni][nj] == 'L' and not visited[ni][nj]:
                    return True
                else:
                    tmp_swan_queue.appendleft((ni, nj))

    return visited[start_end[1][0]][start_end[1][1]]


R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

start_end = []
first_queue = deque()

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'L':
            start_end.append([i, j])
            first_queue.append([i, j])
        elif graph[i][j] == '.':
            first_queue.append([i, j])


result = 0
flag = False

new_queue = deque()

visited_q = [[False]*C for _ in range(R)]

while first_queue:
    i, j = first_queue.popleft()
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < R and 0 <= nj < C:
            if graph[ni][nj] == 'X' and not visited_q[ni][nj]:
                graph[ni][nj] = '.'
                visited_q[ni][nj] = True
                new_queue.append((ni, nj))

result += 1
swan_queue = deque([start_end[0]])
tmp_swan_queue = deque()
visited = [[False]*C for _ in range(R)]
visited[start_end[0][0]][start_end[0][1]] = True
flag = bfs()
swan_queue = tmp_swan_queue
tmp_swan_queue = deque()
if flag:
    print(result)
else:
    while not flag:
        tmp_queue = deque()
        while new_queue:
            i, j = new_queue.popleft()
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    if graph[ni][nj] == 'X' and not visited_q[ni][nj]:
                        graph[ni][nj] = '.'
                        visited_q[ni][nj] = True
                        tmp_queue.append((ni, nj))
        result += 1
        flag = bfs()
        new_queue = tmp_queue
        swan_queue = tmp_swan_queue
        tmp_swan_queue = deque()
    print(result)
