# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하라
# 덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2 != 2+1).
# 한 개의 수를 여러 번 사용할 수 있다.
# 답을 1,000,000,000으로 나눈 나머지를 출력한다.
# 1 <= N <= 200, 1 <= K <= 200, 2초
N, K = map(int, input().split())
MOD = 10 ** 9

# dp[i][j]: i개의 수를 이용해서 합이 j가 되도록 만드는 경우의 수
dp = [[0] * (N + 1) for _ in range(K + 1)]

# dp[i][0]: 합이 0이 되도록 하려는 경우의 수는 1
# dp[1][j]: 1개의 수로 합이 j를 만드는 경우의 수는 1 (하나의 수가 바로 j)
# 1개의 수로 N을 만들기 위한 수는 N
# 이를 바탕으로 초기값 설정
for i in range(K + 1):
    dp[i][0] = 1
for j in range(N + 1):
    dp[1][j] = 1

# 점화식으로 DP 채우기
# dp[i][j] = dp[i-1][j] + dp[i][j-1]
for i in range(2, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

print(dp[K][N])
print(dp)
