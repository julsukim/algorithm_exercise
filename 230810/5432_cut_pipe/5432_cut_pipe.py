import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    pipe = list(input())
    answer = 0

    N = len(pipe)
    stack = []
    for i in range(N):
        if pipe[i] == '(':
            stack.append(pipe[i])
        else:
            if pipe[i-1] == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1

    print(f'#{tc} {answer}')