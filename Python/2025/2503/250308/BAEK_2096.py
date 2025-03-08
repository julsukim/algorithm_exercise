# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# max_dp = [arr[0]] + [[0, 0, 0] for _ in range(N)]
# min_dp = [arr[0]] + [[0, 0, 0] for _ in range(N)]
#
# for i in range(1, N):
#     max_dp[i][0] = arr[i][0] + max(max_dp[i - 1][0], max_dp[i - 1][1])
#     max_dp[i][1] = arr[i][1] + max(max_dp[i - 1][0], max_dp[i - 1][1], max_dp[i - 1][2])
#     max_dp[i][2] = arr[i][2] + max(max_dp[i - 1][1], max_dp[i - 1][2])
#
#     min_dp[i][0] = arr[i][0] + min(min_dp[i - 1][0], min_dp[i - 1][1])
#     min_dp[i][1] = arr[i][1] + min(min_dp[i - 1][0], min_dp[i - 1][1], min_dp[i - 1][2])
#     min_dp[i][2] = arr[i][2] + min(min_dp[i - 1][1], min_dp[i - 1][2])
#
# print(max(max_dp[N - 1]), min(min_dp[N - 1]))

# 메모리 초과

import sys

# 입력 처리
N = int(sys.stdin.readline().strip())
first_row = list(map(int, sys.stdin.readline().split()))

# DP 배열 초기화 (메모리 최적화)
max_dp = first_row[:]
min_dp = first_row[:]

for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())

    # 갱신을 위한 임시 변수
    new_max = [
        a + max(max_dp[0], max_dp[1]),
        b + max(max_dp[0], max_dp[1], max_dp[2]),
        c + max(max_dp[1], max_dp[2])
    ]
    new_min = [
        a + min(min_dp[0], min_dp[1]),
        b + min(min_dp[0], min_dp[1], min_dp[2]),
        c + min(min_dp[1], min_dp[2])
    ]

    # 기존 DP 배열을 갱신
    max_dp = new_max
    min_dp = new_min

# 결과 출력
print(max(max_dp), min(min_dp))


# def recur(i, before, total):
#     global minimum, maximum
#     if i >= N:
#         minimum = min(minimum, total)
#         maximum = max(maximum, total)
#         return
#
#     if before == 0:
#         recur(i+1, 0, total + arr[i][0])
#         recur(i+1, 1, total + arr[i][1])
#     elif before == 2:
#         recur(i+1, 1, total + arr[i][1])
#         recur(i+1, 2, total + arr[i][2])
#     else:
#         recur(i + 1, 0, total + arr[i][0])
#         recur(i + 1, 1, total + arr[i][1])
#         recur(i + 1, 2, total + arr[i][2])
#
#
# # for i in range(3):
# #     recur(0, i, 0)
# #
# # print(maximum, minimum)