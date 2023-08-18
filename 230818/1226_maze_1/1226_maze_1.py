import sys
sys.stdin = open('input2.txt')


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


def bfs(sp, N):
    visited = [[0]*N for _ in range(N)]
    i, j = sp, sp
    enQueue((i, j))
    visited[i][j] = 1
    while not is_empty():
        i, j = deQueue()
        if maze[i][j]==3:
            return 1
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                enQueue((ni, nj))
                visited[ni][nj] = 1

    return 0


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    maze = [list(map(int, input())) for _ in range(N)]
    sp = 1

    queue = [0]*(N*N)
    front = -1
    rear = -1

    ans = bfs(sp, N)
    print(f'#{tc} {ans}')
