def tiling(n):
    global dp
    if n < 3:
        return dp[n]
    else:
        if dp[n] == 0:
            dp[n] = tiling(n-2) + tiling(n-1)
        return dp[n]


N = int(input())

dp = [0]*(N+2)
dp[1] = 1
dp[2] = 2
print(tiling(N) % 10007)
