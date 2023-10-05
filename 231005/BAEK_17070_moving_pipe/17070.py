
gogo = {
    1: [(0, 1), (1, 1)],
    2: [(1, 0), (1, 1)],
    3: [(0, 1), (1, 0), (1, 1)]
}

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
d = 1
cnt = 0
