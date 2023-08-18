import sys
sys.stdin = open('input.txt')


def push(value):
    global top
    top += 1
    stack[top] = value


def pop():
    global top
    tmp = top
    top -= 1
    return stack[tmp]


def is_empty():
    return top == -1


def find_sp(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def dfs(sti, stj, N):
    visited = [[0] * N for _ in range(N)]
    push((sti, stj))
    visited[sti][stj] = 1
    i = sti
    j = stj
    while True:
        if maze[i][j]==3:
            return 1
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N:
                if maze[ni][nj]!=1 and visited[ni][nj]==0:
                    push((ni, nj))
                    visited[ni][nj] = 1
                    i = ni
                    j = nj
                    break
        else:
            if not is_empty():
                i, j = pop()
            else:
                break

    return 0


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    stack = [0] * (N*N)
    top = -1

    sti, stj = find_sp(N)
    ans = dfs(sti, stj, N)
    print(f'#{tc} {ans}')
