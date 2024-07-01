T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    score_list = list(map(int, input().split()))

    total_score = 0    # 얻을 수 있는 총 점수
    for i in range(1, N + 1):    # 튕기는 거리 증가
        for j in range(0, N, i):    # 튕기는 거리에 따른 획득 점수
            total_score += score_list[j]
    if total_score <= 0:    # 획득 점수가 0점 이하인 경우는 0점으로 출력
        total_score = 0

    print(f'#{tc} {total_score}')
