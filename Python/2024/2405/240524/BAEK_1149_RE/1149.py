# import sys
# sys.setrecursionlimit(10000)
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# answer = 10e9
#
#
# def find_min(index, before, cost):
#     global answer
#     if index == N:
#         answer = min(answer, cost)
#         return
#     else:
#         for i in range(3):
#             if before != i:
#                 find_min(index + 1, i, cost + arr[index][i])
#
#
# find_min(0, -1, 0)
# print(answer)

import sys
sys.setrecursionlimit(10000)

N = int(input())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * 4 for _ in range(N)]


def find_min(index, before):
    global answer
    if index == N:
        return 0
    if dp[index][before] != -1:
        return dp[index][before]
    else:
        tmp = 10e9
        for i in range(1, 4):
            if before != i:
                tmp = min(tmp, find_min(index + 1, i) + arr[index][i])
        dp[index][before] = tmp

        return tmp


answer = find_min(0, 0)
print(answer)
