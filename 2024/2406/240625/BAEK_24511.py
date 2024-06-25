from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue = deque()
for i in range(N):
    if A[i] == 0:
        queue.append(B[i])
else:
    if not queue:
        print(*C)
        sys.exit()

for j in range(M):
    queue.appendleft(C[j])
    print(queue.pop(), end=" ")

# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# M = int(input())
# C = list(map(int, input().split()))
#
# # queue = 0, stack = 1
# for i in range(M):
#     num = C[i]
#     for j in range(N):
#         if not A[j]:
#             tmp = B[j]
#             B[j] = num
#             num = tmp
#     else:
#         print(num, end=' ')

# N = int(input())
# A = list(map(int, input().split()))
# B = [deque([int(num)]) for num in input().split()]
# M = int(input())
# C = list(map(int, input().split()))
#
# # queue = 0, stack = 1
# for i in range(M):
#     num = C[i]
#     for j in range(N):
#         if A[j] == 0:
#             B[j].append(num)
#             num = B[j].popleft()
#     else:
#         print(num, end=' ')



# 4
# 0 1 1 0
# 1 2 3 4
# 3
# 2 4 7
#
# 1.
# 초기 : 1 2 3 4
# 자료구조 1 = 큐
# 2 입력
# [1] [2] [3] [4]
# [1, 2] [2] [3] [4]
# [2] [2] [3] [4]
# [2] [2, 1] [3] [4]
# [2] [2] [3] [4]
# [2] [2] [3, 1] [4]
# [2] [2] [3] [4]
# [2] [2] [3] [4, 1]
# [2] [2] [3] [1] -> 4
# 4 입력
# [2, 4] [2] [3] [1]
# [4] [2, 2] [3] [1]
# [4] [2] [3, 2] [1]
# [4] [2] [3] [1, 2] -> 1
# 7입력
# [4, 7] [2] [3] [2]
# [7] [2, 4] [3] [2]
# [7] [2] [3, 4] [2]
# [7] [2] [3] [2, 4] -> 2

# 스택은 무시할 수 있음!
# -> 따라서 초기 : [1] [4]
# 2 입력
# [1, 2] [4]
# [2] [4, 1]
# [2] [1] -> 4
# 4 입력
# [2, 4] [1]
# [4] [1, 2]
# [4] [2] -> 1
# 7 입력
# [4, 7] [2]
# [7] [2, 4]
# [7] [4] -> 2
# 1 4
# 2 1 (4)
# 4 2 (1)
# 7 4 (2)
