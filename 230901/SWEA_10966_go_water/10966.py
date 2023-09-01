import sys
sys.stdin = open('input.txt')


def enqueue(value):
    global rear
    rear += 1
    queue[rear] = value
    return


def dequeue():
    global front
    front += 1
    return queue[front]


def is_empty():
    return front == rear


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wl_map = [input() for _ in range(N)]

    queue = [0] * (N*M+1)
    front = rear = -1
    visited = [[0]*M for _ in range(N)]
    total_move = 0

    for i in range(N):
        for j in range(M):
            if wl_map[i][j] == 'W':
                enqueue((i, j))
                visited[i][j] = 1

    while not is_empty():
        i, j = dequeue()
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0:
                enqueue((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] != 1:
                total_move += visited[i][j] - 1

    print(f'#{tc} {total_move}')

