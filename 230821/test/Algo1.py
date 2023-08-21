import sys
sys.stdin = open('algo1_sample_in.txt')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ballons = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0       # 최대 점수
    min_score = 3600    # 최소 점수

    for i in range(N):
        for j in range(N):
            score = ballons[i][j]           # 현재 점수
            for k in range(1, score + 1):   # 풍선의 점수에 따른 추가 범위 지정
                for l in range(4):          # 상하좌우의 풍선 점수 구하기
                    ni = i + (di[l] * k)
                    nj = j + (dj[l] * k)
                    if (0 <= ni < N) and (0 <= nj < N):     # 배열을 벗어나지 않도록 함
                        score += ballons[ni][nj]
            else:
                if max_score < score:
                    max_score = score       # 최대 점수 구하기
                if min_score > score:
                    min_score = score       # 최소 점수 구하기

    result = max_score - min_score          # 최대 점수 차이 구하기

    print(f'#{tc} {result}')
