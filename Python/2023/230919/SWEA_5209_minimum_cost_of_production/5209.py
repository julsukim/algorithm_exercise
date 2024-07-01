import sys
sys.stdin = open('input.txt')


def minimum_cost(i, v):
    global minimum
    if minimum < v:
        return
    if i == N:
        if minimum > v:
            minimum = v
            return
    else:
        for j in range(N):
            if visited[j] == 0:
                v += costs[i][j]
                visited[j] = 1
                minimum_cost(i+1, v)
                v -= costs[i][j]
                visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    minimum = 1500
    visited = [0]*N

    minimum_cost(0, 0)
    print(f'#{tc} {minimum}')
