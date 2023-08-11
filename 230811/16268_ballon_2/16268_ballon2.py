import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ballons = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    max_flo = 0
    for i in range(N):
        for j in range(M):
            flo = 0
            flo += ballons[i][j]
            for l in range(4):
                ni, nj = i + di[l], j + dj[l]
                if 0 <= ni < N and 0 <= nj < M:
                    flo += ballons[ni][nj]
            if max_flo < flo:
                max_flo = flo

    print(f'#{tc} {max_flo}')