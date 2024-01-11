import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    max_move = 0
    start_point = 0
    for i in range(N):
        for j in range(N):
            p, q = i, j
            cnt = 1

            while True:
                for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    ni, nj = p+di, q+dj
                    if 0<=ni<N and 0<=nj<N and rooms[p][q]+1==rooms[ni][nj]:
                        cnt += 1
                        p, q = ni, nj
                        break
                else:
                    break

            if max_move < cnt:
                max_move = cnt
                start_point = rooms[i][j]
            elif max_move == cnt:
                if start_point > rooms[i][j]:
                    start_point = rooms[i][j]

    print(f'#{tc} {start_point} {max_move}')
