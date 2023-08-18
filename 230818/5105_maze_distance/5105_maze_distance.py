import sys
sys.stdin = open('input.txt')


def enQueue(value):
    global front
    front += 1
    queue[front] = value


def deQueue():
    global rear
    rear += 1
    return queue[rear]


def is_empty():
    return front == rear


def find_sp(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def bfs(sti, stj, N):
    visited = [[0]*N for _ in range(N)]
    enQueue((sti, stj))
    visited[sti][stj] = 1
    while not is_empty():
        i, j = deQueue()
        if maze[i][j] == 3:
            return visited[i][j] - 2
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                enQueue((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    return 0


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    queue = [0] * (N * N)
    front = -1
    rear = -1

    sti, stj = find_sp(N)
    ans = bfs(sti, stj, N)

    print(f'#{tc} {ans}')
