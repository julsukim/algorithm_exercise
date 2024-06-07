import copy
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# maximum = arr[0]
# if N > 1:
#     dp = copy.deepcopy(arr)
#     for i in range(1, N):
#         for j in range(1, i+1):
#             dp[i-j] += arr[i]
#             maximum = max(dp[i-j], maximum)
#     print(maximum)
# else:
#     print(maximum)

maximum = -1000
tmp = 0
for i in range(N):
    maximum = max(maximum, arr[i])
    if tmp + arr[i] >= 0:
        tmp += arr[i]
        maximum = max(maximum, tmp)
    else:
        tmp = 0

print(maximum)
