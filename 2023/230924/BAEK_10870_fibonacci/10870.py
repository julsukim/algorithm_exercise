# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)


# memoization
def fibo2(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = (fibo2(n-1) + fibo2(n-2))
    return memo[n]


# dp
def fibo3(n):
    dp = [0]*(n+2)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


N = int(input())
# print(fibo(N))
# memo = [0]*(N+2)
# memo[0] = 0
# memo[1] = 1
# fibo2(N)
# print(memo[N])
print(fibo3(N))
