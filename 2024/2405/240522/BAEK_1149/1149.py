N = int(input())
rgb_costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = rgb_costs[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb_costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb_costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb_costs[i][2]

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# -> 색이 계속 달라야 함.
# 모든 집을 칠하는 비용의 최솟값 출력
