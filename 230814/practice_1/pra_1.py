import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    exp = input()
    N = len(exp)

    stack = [0] * N
    top = -1
    postfix_like = ''
    for x in exp:
        if x in '+-*/':
            top += 1
            stack[top] = x
        else:
            postfix_like += x
    else:
        while top != -1:
            postfix_like += stack[top]
            top -= 1

    print(f'#{tc} {postfix_like}')