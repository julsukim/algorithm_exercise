import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    exp = input()

    stack = [0] * N
    top = -1
    pri = {'*': 2, '+': 1}

    postfix = ''
    for x in exp:
        if x not in '*+':
            postfix += x

        else:
            if top == -1 or pri[stack[top]] < pri[x]:
                top += 1
                stack[top] = x
            elif pri[stack[top]] >= pri[x]:
                while top > -1 and pri[stack[top]] >= pri[x]:
                    postfix += stack[top]
                    top -= 1
                top += 1
                stack[top] = x

    else:
        while top != -1:
            postfix += stack[top]
            top -= 1
        top -= 1

    for x in postfix:
        if x not in '+*':
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
            else:
                top += 1
                stack[top] = op2 * op1

    print(f'#{tc} {stack[top]}')