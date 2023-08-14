import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    exp = input()
    N = len(exp)

    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

    stack = [0] * N
    top = -1
    postfix = ''
    for x in exp:
        if x not in '+-*/':
            postfix += x
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
    else:
        while top != -1:
            postfix += stack[top]
            top -= 1

    print(f'#{tc} {postfix}')