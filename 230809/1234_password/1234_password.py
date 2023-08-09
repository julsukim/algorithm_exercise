import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N, string = input().split()
    N = int(N)

    stack = [''] * N
    top = -1

    top += 1
    stack[top] = string[0]

    count = 0
    while count < N - 1:
        count += 1
        if stack[top] != string[count]:
            stack[top + 1] = string[count]
            top += 1
        else:
            stack[top] = ''
            top -= 1

    result = ''
    for i in stack:
        result += i
    print(f'#{tc} {result}')