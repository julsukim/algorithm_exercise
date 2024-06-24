import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    num = int(input())
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)
if stack:
    print(sum(stack))
else:
    print(0)
