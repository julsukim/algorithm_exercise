# 금액 최소 지불
# 카드 N개 구매
# 카드가 i개 포함된 카드 팩의 가격은 costs[i]원

N = int(input())
costs = [0] + list(map(int, input().split()))

dp = [1000000000000]*(N+1)
# 카드 1개를 구매하기 위한 최솟값
dp[0] = 0
dp[1] = costs[1]
# 카드 2개를 구매하기 위한 최솟값
# dp[2] = min(dp[1] + costs[1], dp[0] + costs[2])
# dp[3] = min(dp[2] + costs[1], dp[1] + costs[2], dp[0] + costs[3])
# dp[4] = min(dp[3] + costs[1], dp[2] + costs[2], dp[1] + costs[3], dp[0] + costs[4])
# dp[5] = min(dp[4] + costs[1], dp[3] + costs[2], dp[2] + costs[3], dp[1] + costs[4], dp[0] + costs[5])

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + costs[j])

print(dp[N])
