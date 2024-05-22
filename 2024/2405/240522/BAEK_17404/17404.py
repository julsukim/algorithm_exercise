N = int(input())
rgb_costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = rgb_costs[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb_costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb_costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb_costs[i][2]

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))