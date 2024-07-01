import sys
sys.stdin = open('input.txt')

T = 11
for tc in range(1, T+1):
    N = int(input())
    s = input()
    exp = '(' + s + ')'

    stack = [0] * (N+1)
    top = -1
    icp = {'(': 3, '+': 1}
    isp = {'(': 0, '+': 1}

    postfix = ''
    for x in exp:
        if x not in '(+)':
            postfix += x
        elif x == ')':
            while stack[top] != '(':
                postfix += stack[top]
                top -= 1
            top -= 1

        else:
            if top == -1 or isp[stack[top]] < icp[x]:
                top += 1
                stack[top] = x
            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    postfix += stack[top]
                    top -= 1
                top += 1
                stack[top] = x

    print(postfix)

    stack= [0] * (N+1)
    top = -1
    for x in postfix:
        if x != '+':
            top += 1
            stack[top] = int(x)
        else:
            op1 = stack[top]
            top -= 1
            op2 = stack[top]
            top -= 1
            if x == '+':
                top += 1
                stack[top] = op2 + op1

    print(stack[top])