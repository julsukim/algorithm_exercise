import sys
input = sys.stdin.readline

N = int(input())
costs = list(map(int, input().split()))

# 카드 N개를 갖기 위해 지불해야 하는 금액의 최댓값
dp = [0] * (N + 1)

for i in range(1, N + 1):
    # i장 살 때, 1장 팩부터 i장 팩까지 고려
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + costs[j - 1])

print(dp[N])
