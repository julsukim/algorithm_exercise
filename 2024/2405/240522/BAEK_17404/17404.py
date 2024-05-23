N = int(input())
rgb_costs = [list(map(int, input().split())) for _ in range(N)]

INF = 10e9
answer = INF

for start in range(3):
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = [INF, INF, INF]

    dp[0][start] = rgb_costs[0][start]

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb_costs[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb_costs[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb_costs[i][2]

    dp[N-1][start] = INF
    answer = min(answer, min(dp[N-1]))

print(answer)
