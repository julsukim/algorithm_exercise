import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    exp = input()

    stack = [0] * N
    top = -1
    postfix = ''
    for i in exp:
        if i != '+':
            postfix += i
        else:
            if top == -1:
                top += 1
                stack[top] = i
            else:
                while top > -1:
                    postfix += stack[top]
                    top -= 1
                top += 1
                stack[top] = i
    else:
        while top != -1:
            postfix += stack[top]
            top -= 1

    top = -1
    for i in postfix:
        if i != '+':
            top += 1
            stack[top] = int(i)
        else:
            op1 = stack[top]
            top -= 1
            op2 = stack[top]
            top -= 1
            top += 1
            stack[top] = op2 + op1

    print(f'#{tc} {stack[top]}')