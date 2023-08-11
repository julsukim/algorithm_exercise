import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pic = [list(map(int, input().split())) for _ in range(N)]

    max_l = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if pic[i][j] == 1:
                cnt += 1
            else:
                if max_l < cnt:
                    max_l = cnt
                cnt = 0
        else:
            if max_l < cnt:
                max_l = cnt

    for j in range(M):
        cnt = 0
        for i in range(N):
            if pic[i][j] == 1:
                cnt += 1
            else:
                if max_l < cnt:
                    max_l = cnt
                cnt = 0
        else:
            if max_l < cnt:
                max_l = cnt

    print(f'#{tc} {max_l}')