import sys
sys.stdin = open('input.txt')


tunnels = {
    1: [[-1, 0], [0, 1], [1, 0], [0, -1]],
    2: [[-1, 0], [1, 0]],
    3: [[0, 1], [0, -1]],
    4: [[-1, 0], [0, 1]],
    5: [[0, 1], [1, 0]],
    6: [[1, 0], [0, -1]],
    7: [[-1, 0], [0, -1]]
}


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
    N, M, R, C, L = map(int, input().split())
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    queue = [0] * (N*M+1)
    front = rear = -1
    total = 0

    enqueue((R, C))
    visited[R][C] = 1
    while not is_empty():

        p, q = dequeue()
        for di, dj in tunnels[tunnel_map[p][q]]:
            ni, nj = p + di, q + dj
            yy = 0
            if 0 <= ni < N and 0 <= nj < M and tunnel_map[ni][nj] != 0 and visited[ni][nj] == 0:
                for ddi, ddj in tunnels[tunnel_map[ni][nj]]:
                    if ni+ddi == p and nj+ddj == q:
                        yy += 1
                    if yy > 0:
                        enqueue((ni, nj))
                        visited[ni][nj] = visited[p][q] + 1

    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                total += 1

    print(f'#{tc} {total}')