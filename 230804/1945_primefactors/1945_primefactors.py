import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prime_list = [2, 3, 5, 7, 11]
    result_list = []
    for prime in prime_list:
        count = 0
        while N % prime == 0:
            N = N // prime
            count += 1
        result_list.append(count)
    print(f'#{tc}', end=' ')
    for result in result_list:
        print(result, end=' ')
    print()