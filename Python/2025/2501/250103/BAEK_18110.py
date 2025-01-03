import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    if n == 0:
        print(0)
        return

    opinions = [int(input()) for _ in range(n)]

    opinions.sort()
    cut = int(n * 0.15 + 0.5)

    trimmed = opinions[cut: n-cut]
    avg = sum(trimmed) / len(trimmed)
    print(int(avg + 0.5))


solve()

# 문제에서의 반올림이 파이썬의 round()와 달라서 틀렸을 가능성이 있다.
# 파이썬의 반올림 = Banker's rounding : 소수점 .5일 때, '짝수 쪽으로 반올림'
# 일반적 (문제에서) 반올림 = round half away from zero : '0.5 이상이면 무조건 올림' 방식
# 따라서 x를 반올림 할 때, int(x + 0.5) / floor(x + 0.5)를 통해서 일반적인 반올림을 구현할 수 있다.
# round(2.5) = 2, round(3.5) = 4
# int(2.5 + 0.5) = 3, int(3.5 + 0.5) = 4
