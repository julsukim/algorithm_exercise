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
