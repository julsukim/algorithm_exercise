T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    si, sj, fi, fj = map(int, input().split())
    ground_list = [list(map(int, input().split())) for _ in range(N)]

    total_height = 0    # 평탄화 영역의 높이 값의 합
    for i in range(si, fi + 1):
        for j in range(sj, fj + 1):
            total_height += ground_list[i][j]

    area = (fi - si + 1) * (fj - sj + 1)    # 평탄화 영역의 칸 수
    avg = total_height // area    # 평균값(영역의 평탄화 높이)

    flatten = 0    # 평탄화 완료된 영역의 합
    work = 0    # 작업 횟수
    while flatten <= area:    # 평탄화 완료 영역 <= 평탄화 필요 영역(평탄화 작업이 완료될 때 까지)
        for i in range(si, fi + 1):
            for j in range(sj, fj + 1):
                if ground_list[i][j] != avg:    # 목표 높이와 같지 않다면
                    if (avg - ground_list[i][j]) < 0:
                        work += -(avg - ground_list[i][j])    # 작업 횟수 추가
                    else:
                        work += (avg - ground_list[i][j])    # 작업 횟수 추가
                    ground_list[i][j] += (avg - ground_list[i][j])    # 목표 높이에 맞춤
                    flatten += 1    # 평탄화 완료 영역에 추가
                else:    # 목표 높이와 같다면
                    flatten += 1    # 평탄화 완료 영역에 추가

    print(f'#{tc} {work}')