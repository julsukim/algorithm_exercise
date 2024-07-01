# import math
# import sys
# sys.setrecursionlimit(10000000)
#
#
# def recursion(n):
#     global answer
#     if dp[n] != -1:
#         return dp[n]
#     if n == 0:
#         return 0
#     else:
#         tmp = 10e9
#         for i in range(1, int(math.sqrt(n))+1):
#             tmp = min(tmp, recursion(n-(i**2)) + 1)
#     dp[n] = tmp
#     return tmp
#
#
# N = int(input())
# dp = [-1]*(N+1)
#
# answer = recursion(N)
# print(answer)

import math

N = int(input())
dp = [float('inf')] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j**2] + 1)

print(dp[N])

# for num in range(316, 0, -1):
#     while True:
#         if (target - num ** 2) >= 0:
#             target -= num ** 2
#             count += 1
#         else:
#             break
#
# print(count)
