import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    postfix = list(input().split())
    N = len(postfix)

    stack = [0] * N
    top = -1
    print(f'#{tc}', end=' ')
    for x in postfix:
        if x not in '+-*/.':
            top += 1
            stack[top] = int(x)
        elif x in '+-*/' and top > 0:
            op1 = stack[top]
            top -= 1
            op2 = stack[top]
            top -= 1
            if x == '+':
                top += 1
                stack[top] = op2 + op1
            elif x == '*':
                top += 1
                stack[top] = op2 * op1
            elif x == '/':
                top += 1
                stack[top] = op2 // op1
            elif x == '-':
                top += 1
                stack[top] = op2 - op1
        elif x in '+-*/' and top <= -1:
            print('error')
            break
        elif x == '.':
            if top == 0:
                print(stack[top])
                break
            else:
                print('error')
                break
        else:
            print('error')
            break
