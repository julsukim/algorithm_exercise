import sys
input = sys.stdin.readline


N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]
for idx in range(1, N+1):
    for weight in range(1, K+1):
        if weight < items[idx-1][0]:
            dp[idx][weight] = dp[idx-1][weight]
        else:
            dp[idx][weight] = max(dp[idx - 1][weight - items[idx-1][0]] + items[idx-1][1], dp[idx - 1][weight])

print(dp[N][K])

# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline
#
#
# def recur(idx, weight):
#
#     if weight > K:
#         return -9999999
#
#     if idx == N:
#         return 0
#
#     if dp[idx][weight] != -1:
#         return dp[idx][weight]
#
#     dp[idx][weight] = max(recur(idx+1, weight + items[idx][0]) + items[idx][1], recur(idx+1, weight))
#     return dp[idx][weight]
#
#
# N, K = map(int, input().split())
# items = [list(map(int, input().split())) for _ in range(N)]
#
# dp = [[-1 for _ in range(100_001)] for _ in range(N)]
# ans = recur(0, 0)
# print(ans)


# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline
#
#
# def recur(idx, weight, value):
#     global answer
#     if weight > K:
#         return
#
#     if idx == N:
#         answer = max(answer, value)
#         return
#
#     recur(idx+1, weight + items[idx][0], value + items[idx][1])
#     recur(idx+1, weight, value)
#
#
# N, K = map(int, input().split())
# items = [list(map(int, input().split())) for _ in range(N)]
# answer = 0
# recur(0, 0, 0)
# print(answer)
