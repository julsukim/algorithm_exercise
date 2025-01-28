import sys
input = sys.stdin.readline

N, H = map(int, input().split())

# 석순·종유석 높이 카운트 테이블
countBottom = [0]*(H+1)  # 인덱스: 석순의 "크기"
countTop = [0]*(H+1)  # 인덱스: 종유석의 "크기"

for i in range(N):
    size = int(input())
    if i % 2 == 0:
        # 석순
        countBottom[size] += 1
    else:
        # 종유석
        countTop[size] += 1

# prefixBottom[h] = 높이 h 이상인 석순의 수
# prefixTop[h]    = 높이 h 이상인 종유석의 수
# 뒤에서부터 누적합
for h in range(H-1, 0, -1):
    countBottom[h] += countBottom[h+1]
    countTop[h]    += countTop[h+1]

min_obstacles = N  # 부딪히는 장애물 최소값(최대치로 초기화)
cnt = 0            # 그 최소값이 등장하는 구간 수

for h in range(1, H+1):
    # 높이 h 구간을 선택했을 때:
    obstacles = countBottom[h] + countTop[H-h+1]
    if obstacles < min_obstacles:
        min_obstacles = obstacles
        cnt = 1
    elif obstacles == min_obstacles:
        cnt += 1

print(min_obstacles, cnt)
