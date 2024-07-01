T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    total_sum = 0
    for i in range(N):
        for j in range(N):
            cur = arr[i][j]
            abs_sum = 0
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    ab = cur - arr[ni][nj]
                    if ab < 0:
                        ab = -ab
                    abs_sum += ab
            total_sum += abs_sum

    print(f'#{tc} {total_sum}')