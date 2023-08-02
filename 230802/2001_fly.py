T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]


    max_kill = 0
    for i in range(N):
        for j in range(N):
            cur = fly_list[i][j]
            kill = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    if 0 <= k < N and 0 <= l < N:
                        kill += fly_list[k][l]
            if kill > max_kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')
