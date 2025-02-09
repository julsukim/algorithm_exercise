N, M = map(int, input().split())

dp = [[0] * M for _ in range(N)]
dp[0][0] = 1
for i in range(1, M):
    dp[0][i] = 1
for i in range(1, N):
    dp[i][0] = 1

MOD = 10 ** 9 + 7
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]) % MOD

print(dp[N-1][M-1] % MOD)
