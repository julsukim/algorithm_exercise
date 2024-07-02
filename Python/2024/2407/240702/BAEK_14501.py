import sys
input = sys.stdin.readline


N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*(N+1)

for idx in range(N)[::-1]:
    if idx + schedule[idx][0] > N:
        dp[idx] = dp[idx+1]
    else:
        dp[idx] = max(dp[idx + schedule[idx][0]] + schedule[idx][1], dp[idx+1])

print(dp[0])


# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
#
# def recur(idx):
#     if idx > N-1:
#         if idx > N:
#             return -99999999
#         return 0
#
#     if dp[idx] != -1:
#         return dp[idx]
#
#     dp[idx] = max(recur(idx+schedule[idx][0]) + schedule[idx][1], recur(idx+1))
#     return dp[idx]
#
#
# N = int(input())
# schedule = [list(map(int, input().split())) for _ in range(N)]
#
# dp = [-1]*N
# recur(0)
# print(dp[0])


# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
#
# def recur(idx, cost):
#     global answer
#
#     if idx > N-1:
#         if idx > N:
#             return
#         answer = max(answer, cost)
#         return
#
#     recur(idx+schedule[idx][0], cost+schedule[idx][1])
#
#     recur(idx+1, cost)
#
#
# N = int(input())
# schedule = [list(map(int, input().split())) for _ in range(N)]
# answer = -1
# recur(0, 0)
# print(answer)
