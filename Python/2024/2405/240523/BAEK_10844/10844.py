# 쉬운 계단 수
# 길이가 N인 계단 수의 갯수 구하기
# 끝 수가 value인 dp 테이블 작성
# 이전 끝 수가 9, 0인 경우 처리

N = int(input())
dp = [[0] * 10 for _ in range(N)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N-1]) % 1000000000)
