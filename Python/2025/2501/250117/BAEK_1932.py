import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]


def recur(row, col):
    if row >= N-1:
        return 0

    if dp[row][col] != -1:
        return dp[row][col]

    dp[row][col] = max(recur(row + 1, col) + triangle[row + 1][col],
                       recur(row + 1, col + 1) + triangle[row + 1][col + 1])

    return dp[row][col]


dp = [[-1] * N for _ in range(N)]
print(recur(0, 0) + triangle[0][0])
