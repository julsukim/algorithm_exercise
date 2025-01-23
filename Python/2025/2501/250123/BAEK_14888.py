# 0: +, 1: -, 2: *, 3: //
# 나눗셈은 정수 나눗셈. 음수를 양수로 나눌 때는 C++14의 기준을 따른다.
# 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼다.
# 연산자를 넣은 결과의 최대 / 최소를 구하라
# 계산은 우선 순위 없이, 앞에서부터 진행

import sys
sys.setrecursionlimit(10**6)

N = int(input())
sequence = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))
operators = ['+'] * operator_cnt[0]
operators.extend(['-'] * operator_cnt[1])
operators.extend(['*'] * operator_cnt[2])
operators.extend(['//'] * operator_cnt[3])

maximum = -(10**10)
minimum = 10**10


def permutation(i):
    global maximum, minimum

    if i == N-1:
        value = sequence[0]
        operator_i = 0
        for i in range(1, N):
            if operators[operator_i] == '+':
                value += sequence[i]
            elif operators[operator_i] == '-':
                value -= sequence[i]
            elif operators[operator_i] == '*':
                value *= sequence[i]
            elif operators[operator_i] == '//':
                if value < 0:
                    value = -((-value) // sequence[i])
                elif value >= 0:
                    value = value // sequence[i]
            operator_i += 1
        maximum = max(maximum, value)
        minimum = min(minimum, value)
        return

    for swap_i in range(i, N-1):
        operators[i], operators[swap_i] = operators[swap_i], operators[i]
        permutation(i+1)
        operators[i], operators[swap_i] = operators[swap_i], operators[i]


permutation(0)
print(maximum)
print(minimum)
