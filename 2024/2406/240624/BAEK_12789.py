import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
now = 1

for i in range(N):
    while stack and stack[-1] == now:
        stack.pop()
        now += 1
    if arr[i] == now:
        now += 1
    else:
        stack.append(arr[i])

while stack and stack[-1] == now:
    stack.pop()
    now += 1

if now - 1 == N:
    print("Nice")
else:
    print("Sad")

# for i in range(N):
#     if now == arr[i]:
#         now += 1
#     else:
#         if stack:
#             if stack[-1] == now:
#                 stack.pop()
#                 now += 1
#             elif stack[-1] > arr[i]:
#                 stack.append(arr[i])
#             else:
#                 print("Sad")
#                 break
#         else:
#             stack.append(arr[i])
# else:
#     print("Nice")
