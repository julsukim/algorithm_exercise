import sys
sys.stdin = open('input.txt')


def postfix_notation(string):
    numbers = '0123456789'
    postfix = ''
    stack = []
    # 숫자는 출력
    for token in string:
        if token in numbers:
            postfix += token
        else:
            if len(stack):    # stack에 + 연산자가 있다면 (현재 stack에 들어갈 수 있는 것은 + 뿐)
                postfix += stack.pop()
            stack.append(token)

    return postfix + stack.pop()
    # 연산자는 stack 에 push (더하기 연산자 밖에 없음) 고려할 우선순위가 없다.

def postfix_calculator(notation):
    numbers = '0123456789'
    stack = []

    for token in notation:
        if token in numbers:
            stack.append(token)
        else:
            value2 = int(stack.pop())
            value1 = int(stack.pop())
            stack.append(value1 + value2)

    return stack.pop()

T = 10
for tc in range(1, T+1):
    N = int(input())
    exp = input()

    # stack = [0] * N
    # top = -1
    #
    # postfix = ''
    # for x in exp:
    #     if x != '+':
    #         postfix += x
    #
    #     else:
    #         if top == -1:
    #             top += 1
    #             stack[top] = x
    #         else:
    #             while top > -1:
    #                 postfix += stack[top]
    #                 top -= 1
    #             top += 1
    #             stack[top] = x
    #
    # else:
    #     while top != -1:
    #         postfix += stack[top]
    #         top -= 1

    postfix = postfix_notation(exp)
    result = postfix_calculator(postfix)
    print(f'#{tc} {result}')
    print(postfix)