import sys
input = sys.stdin.readline

dp = [0] * (100 + 1)
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i - 3] + dp[i - 2]

T = int(input())
result = [str(dp[int(input())]) for _ in range(T)]

print('\n'.join(result))
