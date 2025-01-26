N, K = map(int, input().split())

MOD = 10 ** 9
# 1개로 N => N
# 조건 N 합, K 갯수 -> 경우의 수
dp = [[0] * (N+1) for _ in range(K+1)]

# dp[K][N] : K개의 수로 N이 되도록 만드는 경우의 수
for i in range(K+1):
    dp[i][0] = 1
for i in range(N+1):
    dp[1][i] = 1

for i in range(2, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

print(dp[K][N])
