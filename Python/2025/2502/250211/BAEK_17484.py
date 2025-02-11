import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
# dp[i][j][d]: i번째 행, j번째 열에 도달할 때, 마지막 이동 방향 d에서의 최소 연료 소비량
dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

# 첫 행에서 출발해 바로 1행으로 이동하는 경우를 초기화
for j in range(M):
    for d in range(3):
        new_j = j + (d - 1)  # d=0 -> j-1, d=1 -> j, d=2 -> j+1
        if 0 <= new_j < M:
            dp[1][new_j][d] = min(dp[1][new_j][d], grid[0][j] + grid[1][new_j])

# 1행부터 N-2행까지 DP를 진행 (마지막 행은 N-1)
for i in range(1, N - 1):
    for j in range(M):
        for prev_d in range(3):
            if dp[i][j][prev_d] == INF:
                continue
            for d in range(3):
                if d == prev_d:  # 같은 방향 연속 이동은 불가
                    continue
                new_j = j + (d - 1)
                if 0 <= new_j < M:
                    new_cost = dp[i][j][prev_d] + grid[i + 1][new_j]
                    dp[i + 1][new_j][d] = min(dp[i + 1][new_j][d], new_cost)

# 마지막 행에서의 최소 연료 소비량 구하기
answer = INF
for j in range(M):
    for d in range(3):
        answer = min(answer, dp[N - 1][j][d])

print(answer)
