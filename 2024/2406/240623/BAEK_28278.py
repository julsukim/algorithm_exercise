import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        if stack:
            num = stack.pop()
            print(num)
        else:
            print(-1)
    elif order[0] == 3:
        print(len(stack))
    elif order[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            num = stack[-1]
            print(num)
        else:
            print(-1)
