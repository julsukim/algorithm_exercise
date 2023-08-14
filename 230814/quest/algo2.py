'''
stack에 리스트의 요소를 하나씩 넣기..
닫힌 괄호가 등장하면 마지막 요소를 pop하여 닫힌 괄호에 맞는 연산하기..
하나씩 pop하며 연산하고, str타입이 등장했을때, 요소가 짝이 맞는 지 검사하기..
짝이 맞다면 열린괄호 pop하고 연산 결과를 push하고,
다시 리스트 요소 push 시작하기.
짝이 틀리면 -1, break.
성급하게 풀지 말고 방법을 생각한 후에 풀기...
pop, push를 잘 활용하기,, while 활용하기,,,
'''

import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    str_arr = input()

    open_br = ['(', '{']
    close_br = [')', '}']

    arr = []
    for i in str_arr:    # 주어진 수식을 리스트로 변환
        if (i not in open_br) and (i not in close_br):
            arr.append(int(i))
        else:
            arr.append(i)

    stack = []
    result = -1
    for i in range(len(arr)):
        if (arr[i] not in open_br) and (len(stack) == 0):
            result = -1
            break

        elif arr[i] in close_br:
            r = stack.pop()
            if arr[i] == ')':
                while True:
                    if type(stack[-1]) == str:
                        if stack[-1] != '(':
                            result = -1
                            break
                        else:
                            stack.pop()
                            stack.append(r)
                            break
                    else:
                        r += stack.pop()
            else:
                while True:
                    if type(stack[-1]) == str:
                        if stack[-1] != '{':
                            result = -1
                            break
                        else:
                            stack.pop()
                            stack.append(r)
                            break
                    else:
                        r = r * stack.pop()

        else:
            stack.append(arr[i])

    else:
        if len(stack) == 1:
            result = stack[-1]


    print(f'#{tc} {result}')