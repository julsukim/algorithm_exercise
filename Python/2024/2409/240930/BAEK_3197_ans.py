from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while swan_queue:
        i, j = swan_queue.popleft()
        for di, dj in directions:
            ni = i + di
            nj = j + dj
            if 0 <= ni < R and 0 <= nj < C and not swan_visited[ni][nj]:
                swan_visited[ni][nj] = True
                if graph[ni][nj] == '.':
                    swan_queue.append((ni, nj))
                elif graph[ni][nj] == 'L':
                    return True
                else:  # graph[ni][nj] == 'X'
                    swan_next_queue.append((ni, nj))
    return False

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

start_end = []
water_queue = deque()
swan_queue = deque()
swan_visited = [[False]*C for _ in range(R)]
water_visited = [[False]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if graph[i][j] != 'X':
            water_queue.append((i, j))
            water_visited[i][j] = True
        if graph[i][j] == 'L':
            start_end.append((i, j))

swan_queue.append(start_end[0])
swan_visited[start_end[0][0]][start_end[0][1]] = True

directions = [(-1,0),(1,0),(0,-1),(0,1)]
day = 0
found = False

while not found:
    swan_next_queue = deque()
    found = bfs()
    if found:
        print(day)
        break
    water_next_queue = deque()
    while water_queue:
        i, j = water_queue.popleft()
        for di, dj in directions:
            ni = i + di
            nj = j + dj
            if 0 <= ni < R and 0 <= nj < C and not water_visited[ni][nj]:
                water_visited[ni][nj] = True
                if graph[ni][nj] == 'X':
                    graph[ni][nj] = '.'
                    water_next_queue.append((ni, nj))
    water_queue = water_next_queue
    swan_queue = swan_next_queue
    day += 1
