import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    max_move = 0
    start_point = 0
    count_list = [0] * (N*N+1)
    for i in range(N):
        for j in range(N):
            for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N and rooms[i][j]+1 == rooms[ni][nj]:
                    count_list[rooms[i][j]] = 1
    cnt = 1
    for i in range(N*N, 0, -1):
        if count_list[i] == 1:
            cnt += 1
            if max_move < cnt:
                max_move = cnt
                start_point = i
            elif max_move == cnt:
                start_point = i
        else:
            cnt = 1

    print(f'#{tc} {start_point} {max_move}')
