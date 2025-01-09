from collections import deque
# 올바른 괄호열 X, Y
# () : 2
# [] : 3
# XY = X + Y
# (X) = 2 * X
# [X] = 3 * X
def solve():
    brackets = input().rstrip()

    stack = []
    for ch in brackets:
        # 여는 괄호 '(' 또는 '[' 는 그대로 push
        if ch == '(' or ch == '[':
            stack.append(ch)
        else:
            # 닫는 괄호일 경우
            if not stack:
                # 스택이 비어있으면 짝이 맞지 않음
                print(0)
                return

            if ch == ')':
                # ')'에 대응되는 여는 괄호 '('을 찾아야 한다.
                temp_sum = 0

                # 스택을 pop하면서 내부값 합산
                while stack:
                    top = stack.pop()
                    # 만약 '('를 만나면 내부 합산 종료
                    if top == '(':
                        # 내부값이 없다면 기본값 2, 있으면 2 * temp_sum
                        stack.append(2 if temp_sum == 0 else 2 * temp_sum)
                        break
                    # 숫자라면 temp_sum에 누적
                    elif isinstance(top, int):
                        temp_sum += top
                    else:
                        # '('도 아니고 숫자도 아니라면 (ex. '[' ) 괄호 형태가 잘못됨
                        print(0)
                        return
                else:
                    # while문이 정상 종료가 아니라 stack이 비어서 빠져나온 경우
                    # '('를 찾지 못했다는 의미이므로 잘못된 괄호열
                    print(0)
                    return

            elif ch == ']':
                # ']' 에 대응되는 여는 괄호 '['를 찾아야 한다.
                temp_sum = 0

                while stack:
                    top = stack.pop()
                    if top == '[':
                        # 내부값이 없다면 기본값 3, 있으면 3 * temp_sum
                        stack.append(3 if temp_sum == 0 else 3 * temp_sum)
                        break
                    elif isinstance(top, int):
                        temp_sum += top
                    else:
                        print(0)
                        return
                else:
                    # '['를 찾지 못했다면 잘못된 괄호열
                    print(0)
                    return

    # 모든 처리가 끝난 뒤, 스택에 숫자만 남아있어야 올바른 괄호열
    result = 0
    for val in stack:
        if isinstance(val, int):
            result += val
        else:
            # 만약 여전히 괄호가 남아있다면 잘못된 괄호열
            print(0)
            return

    print(result)


solve()
