import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    repeated = input()
    N = len(repeated)
    stack = [''] * N
    top = -1

    top += 1
    stack[top] = repeated[0]

    count = 0
    while count < N-1:
        count += 1
        if stack[top] != repeated[count]:
            stack[top+1] = repeated[count]
            top += 1
        else:
            stack[top] = ''
            top -= 1

    result = ''
    for i in stack:
        result += i
    print(f'#{tc} {len(result)}')