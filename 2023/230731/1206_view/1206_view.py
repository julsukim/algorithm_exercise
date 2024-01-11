import sys
sys.stdin = open('input.txt')
'''
T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    views = 0

    for i in range(2, N - 2):
        view_list = []
        left1 = arr[i] - arr[i - 1]
        left2 = arr[i] - arr[i - 2]
        right1 = arr[i] - arr[i + 1]
        right2 = arr[i] - arr[i + 2]
        view_list.append(left1)
        view_list.append(left2)
        view_list.append(right1)
        view_list.append(right2)
        if left1 >= 1 and left2 >= 1 and right1 >= 1 and right2 >= 1:
            min_v = view_list[0]
            for v in view_list:
                if min_v > v:
                    min_v = v
            views += min_v

    print(f'#{tc} {views}')
'''
# 본인 높이 - (좌 우 중 가장 높은 빌딩) => 확보된 조망권 -> 누적
T = 10
for tc in range(1, T+1):
    N = int(input())
    building_list = list(map(int, input().split()))

    # 1. 좌, 우 끝은 빌딩이 없다.
    # 2. 형재 빌딩에서 좌, 우 2칸 씩 빌딩의 높이를 찾는다.
    # 2-1. 그 중에서 가장 높은 빌딩의 층수를 구한다. (max 값)
    # 2-2. 만약 빌딩이 없는 경우는 그냥 continue로 넘어간다.
    # 3. 나의 현재 빌딩 높이보다 낮으면 (미만) 조망권이 있는 경우
    # 3-1. 현재 빌딩 높이 - 가장 높은 주변 빌딩 높이 = 조망권이 있는 층의 개수
    # 3-2. 조망권의 층의 개수를 누적한다.
    # 4. 다음 빌딩을 선택한 후, 다시 2번 부터 반복한다.

    # for building in building_list:
    # 이렇게 반복하게 되면 좌, 우 2칸 씩 확인하는 것이 번거로울 수 있다.
    # -> enumerate 사용
    # 현재 위치가 어딘지 모르기 때문.(현재위치 == index 번호)

    total = 0
    for idx in range(N): # 빌딩의 개수
        if not building_list[idx] == 0: # 빌딩이 없으면 다음 빌딩
            continue

        current_building = building_list[idx] # 현재 빌딩
        # 빌딩이 있는 경우 좌 우 2칸 씩 확인하자
        delta = [-2, -1, 1, 2]
        max_height = 0 # 가장 높은 빌딩을 저장하는 변수
        for i in range(4):
            # 가장 높은 빌딩인지 확인
            if max_height < building_list[idx + delta[i]]:
                max_height = building_list[idx + delta]

        # 가장 높은 빌딩과 현재 빌딩을 비교해서 조망원이 있는 지 확인