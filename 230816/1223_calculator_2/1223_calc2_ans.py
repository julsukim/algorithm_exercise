import sys
sys.stdin = open('input.txt')


def push(value):
    # 글로벌 변수를 수정하기 위해서는 global 선언이 필요
    # (list, dict는 리스트 주소를 가리키기 때문에 그냥 수정 가능)
    global top
    top += 1
    stack[top] = value


def pop():
    global top
    tmp = stack[top]
    top -= 1
    return tmp


def is_empty():
    return top == -1


def make_postfix_notation(infix):
    numbers = '0123456789'
    icp = {'+': 1, '*': 2}
    isp = {'+': 1, '*': 2}

    postfix = ''

    for token in infix:
        if token in numbers:    # 숫자라면 출력 postfix에 붙인다.
            postfix += token
        else:    # 연산자 +, *
            # 토근의 연산자 순위가 높을 때 까지 stack을 pop할 것임
            # icp : 토큰의 연산자 우선 순위
            # isp : 스택에 든 연산자 우선 순위
            # 원하는 것 : 스택에 있는 연산자가 token의 연산자 우선순위보다 낮아야 함
            # 해야할 것
            # 스택에 있는 연산자 우선 순위가 토큰보다 같거나 크다면 pop해서 제거하기
            # 그리고 token을 stack에 넣어주기
            while not is_empty() and icp[token] <= isp[stack[top]]:
                postfix += pop()
            push(token)
    # 모든 token 확인이 끝나면
    # stack에 남아있는 연산자도 pop해서 postfix에 붙여주자
    while not is_empty():
        postfix += pop()

    return postfix


def calc_postfix_notation(postfix):
    numbers = '0123456789'

    for token in postfix:
        if token in numbers:    # 숫자는 push
            push(token)
        else:
            val2 = int(pop())
            val1 = int(pop())
            if token == '*':
                push(val1 * val2)
            elif token == '+':
                push(val1 + val2)
    # 모든 token을 확인하면
    # stack에는 1개의 값만 남게 될 것 (결과 값)
    return pop()


T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()

    top = -1    # 전역 변수로 처리
    stack = [0] * N    # 충분한 길이

    # postfix = make_postfix_notation('3+4*2')    # 342*+
    # print(postfix)

    postfix = make_postfix_notation(infix)
    result = calc_postfix_notation(postfix)
    print(f'#{tc} {result}')