di = [-1, 0, 1, 0]    # 특정 지역의 인접지역 파악을 위한 델타 리스트
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            count = 0
            for k in range(4):    # 인접 지역을 탐색하며 높이를 확인
                ni = i + di[k]
                nj = j + dj[k]
                if (0 <= ni < N) and (0 <= nj < N):    # 리스트 내의 인접지역만 탐색
                    if map_list[i][j] <= map_list[ni][nj]:
                        count += 1
            if count == 0:
                result += 1

    print(f'#{tc} {result}')