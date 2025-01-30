import sys
sys.setrecursionlimit(10**9)

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


def fibonacci(n):
    cnt2 = 0
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        cnt2 += 1
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n], cnt2


N = int(input())

cnt1, cnt2 = fibonacci(N)

print(cnt1, cnt2)
