import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    degree_90 = [[0] * N for _ in range(N)]
    degree_180 = [[0] * N for _ in range(N)]
    degree_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            degree_90[j][(N-1)-i] = num_list[i][j]
            degree_180[(N-1)-i][(N-1)-j] = num_list[i][j]
            degree_270[(N-1)-j][i] = num_list[i][j]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(degree_90[i][j], end='')
        print(' ', end='')
        for j in range(N):
            print(degree_180[i][j], end='')
        print(' ', end='')
        for j in range(N):
            print(degree_270[i][j], end='')
        print(' ', end='')
        print()
