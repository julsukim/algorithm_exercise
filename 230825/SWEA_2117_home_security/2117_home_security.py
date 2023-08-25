import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N):
        for j in range(N):
            if city[i][j]==1:
                cnt = 1
            else:
                cnt = 0
            for k in range(N*N):
                for l in range(0, k):
                    if 0<=i-k+l<N and 0<=j+l<N:
                        if city[i-k+l][j+l]==1:
                            cnt += 1
                    if 0<=i+l<N and 0<=j+k-l<N:
                        if city[i+l][j+k-l]==1:
                            cnt += 1
                    if 0<=i+k-l<N and 0<=j-l<N:
                        if city[i+k-l][j-l]==1:
                            cnt += 1
                    if 0<=i-l<N and 0<=j-k+l<N:
                        if city[i-l][j-k+l]==1:
                            cnt += 1

                if (k+1)**2 + k**2 <= cnt*M:
                    if max_cnt < cnt:
                        max_cnt = cnt

    print(f'#{tc} {max_cnt}')
