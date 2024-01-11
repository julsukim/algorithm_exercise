import sys
sys.stdin = open('input.txt')


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def bfs(sti, stj, N):
    visited = [[0] * N for _ in range(N)]   # visited 생성
    queue = []                              # queue 생성
    queue.append((sti, stj))                 # 시작점 enQ
    visited[sti][stj] = 1                   # 시작점 enQ 표시
    while queue:
        i, j = queue.pop(0)
        if maze[i][j]==3:
            return visited[i][j] - 2        # 지나온 칸 수 리턴
        # 인접하고 enQ된 적이 없으면...
        # enQ, visited 표시
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0                                # 3인 칸에 도달할 수 없는 경우


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')
