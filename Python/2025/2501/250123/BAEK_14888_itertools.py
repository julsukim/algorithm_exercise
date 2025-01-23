import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
sequence = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))
ops = ['+', '-', '*', '//']
operators = []
for op, cnt in zip(ops, operator_cnt):
    operators.extend([op] * cnt)

maximum = -10**9
minimum = 10**9


def int_div(a, b):
    if a < 0:
        return -((-a) // b)
    return a // b


for perm in set(permutations(operators)):
    value = sequence[0]
    oi = 0
    for i in range(1, N):
        if perm[oi] == '+':
            value += sequence[i]
        elif perm[oi] == '-':
            value -= sequence[i]
        elif perm[oi] == '*':
            value *= sequence[i]
        elif perm[oi] == '//':
            value = int_div(value, sequence[i])
        oi += 1

    maximum = max(maximum, value)
    minimum = min(minimum, value)

print(maximum)
print(minimum)
