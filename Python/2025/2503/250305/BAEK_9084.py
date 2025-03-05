import sys
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    costs = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1
    for cost in costs:
        for i in range(cost, M + 1):
            dp[i] = dp[i] + dp[i - cost]

    result.append(str(dp[M]))

print('\n'.join(result))
