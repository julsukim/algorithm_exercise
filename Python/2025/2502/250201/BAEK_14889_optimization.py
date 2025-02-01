import sys
from itertools import combinations

# 입력 받기
input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

players = range(N)
min_diff = float('inf')

# 팀을 N/2명씩 고르는 모든 조합에 대해 반복
for team1 in combinations(players, N // 2):
    # team1에 속하지 않는 선수들은 team2가 됨
    team2 = [p for p in players if p not in team1]

    score1, score2 = 0, 0

    # team1 내부의 모든 쌍에 대해 능력치 합을 구함
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            score1 += S[team1[i]][team1[j]] + S[team1[j]][team1[i]]

    # team2 내부의 모든 쌍에 대해 능력치 합을 구함
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            score2 += S[team2[i]][team2[j]] + S[team2[j]][team2[i]]

    # 두 팀의 능력치 차이의 최솟값 갱신
    diff = abs(score1 - score2)
    if diff < min_diff:
        min_diff = diff

    # 차이가 0이면 더 이상 줄일 수 없으므로 바로 종료
    if min_diff == 0:
        break

print(min_diff)
