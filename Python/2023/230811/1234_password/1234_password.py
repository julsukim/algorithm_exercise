'''
왼쪽에서 오른쪽으로 가면서..
왼쪽 원소가 같으면 지워주기
stack으로 풀기
stack이 비어있으면 push
비어있지않고 top과 다르면 push
->
stack이 비어있거나 top과 다르면 push
else: (stack이 비어있지 않고 top과 같으면)
pop
...
'''
import sys
sys.stdin = open('input.txt')

'''
# stack 길이 지정

T = 10
for tc in range(1, T+1):
    str_N, str_num = input().split()

    N = int(str_N)
    stack = [0] * N
    top = -1

    for t in str_num:
        if (top == -1) or (stack[top] != t): # 스택이 비어있거나, top원소와 다르면
            top += 1 # push(t)
            stack[top] = t
        else: # 스택이 비어있지 않고, top과 같으면
            top -= 1

    # ans = ''
    # for i in range(top+1):
    #     ans += stack[i]
    # print(f'#{tc} {ans}')

    ans = ''.join(stack[:top+1])
    print(f'#{tc} {ans}')
'''
# 빈 stack 사용

T = 10
for tc in range(1, T+1):
    str_N, str_num = input().split()

    N = str_N
    stack = []

    for t in str_num:
        if (stack == []) or (stack[-1] != t):
            stack.append(t)
        else:
            stack.pop()

    ans = ''.join(stack[:])
    print(f'#{tc} {ans}')