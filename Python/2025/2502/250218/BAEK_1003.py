# import sys
# sys.setrecursionlimit(100000)
# T = int(input())
#
#
# def fibonacci(n):
#     global zero, one
#     if n == 0:
#         zero += 1
#         return 0
#     elif n == 1:
#         one += 1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# answers = []
# for _ in range(T):
#     N = int(input())
#     zero = 0
#     one = 0
#     fib = fibonacci(N)
#     answers.append(f'{zero} {one}')
#
# print('\n'.join(answers))

T = int(input())
answers = []

dp = [0] * 41
dp[0] = 0
dp[1] = 1
for i in range(2, 41):
    dp[i] = dp[i - 1] + dp[i - 2]

for _ in range(T):
    N = int(input())
    if N == 0:
        answers.append('1 0')
    elif N == 1:
        answers.append('0 1')
    else:
        answers.append(f'{dp[N - 1]} {dp[N]}')

print(*answers, sep='\n')
