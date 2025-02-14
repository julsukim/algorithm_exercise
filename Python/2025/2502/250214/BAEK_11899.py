import sys
input = sys.stdin.readline

S = list(input())

stack = []
for c in S:
    if stack:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            elif stack[-1] == ')':
                stack.append(c)
    elif not stack:
        stack.append(c)

print(len(stack))
