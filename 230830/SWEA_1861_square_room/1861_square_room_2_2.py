import sys
sys.stdin = open('input.txt')


def bfs(i, j, N):
    queue.append((i, j))
    cnt = 0
    while queue:
        i, j = queue.pop(0)
        cnt += 1

        if visited[i][j] != 0:
            return cnt + visited[i][j]-1

        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and rooms[i][j]+1 == rooms[ni][nj]:
                queue.append((ni, nj))

    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    queue = []

    max_move = 0
    start_point = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = bfs(i, j, N)
                move = visited[i][j]
                if max_move < move:
                    max_move = move
                    start_point = rooms[i][j]
                elif max_move == move:
                    if start_point > rooms[i][j]:
                        start_point = rooms[i][j]

    print(f'#{tc} {start_point} {max_move}')
