'''
로직은 맞지만, 시간 초과.
'''
import sys
sys.stdin = open('input.txt')


def my_perm(time):
    global max_v
    if time == L:
        value = int(''.join(numbers))
        if max_v < value:
            max_v = value
        return
    else:
        for i in range(N):
            for j in range(i+1, N):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                my_perm(time+1)     # 횟수 증가
                numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
for tc in range(1, T+1):
    numbers, L = input().split()
    # 교환을 위해 문자열이 아닌 리스트로
    numbers = list(numbers)
    N = len(numbers)
    L = int(L)

    max_v = 0
    my_perm(0)
    print(max_v)
