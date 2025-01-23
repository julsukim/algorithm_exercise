import sys
sys.setrecursionlimit(10**7)

def calc(op, a, b):
    """ a (op) b 를 계산하는 함수.
        op는 '+', '-', '*', '//' 중 하나이고,
        문제 요구사항에 맞춰 나눗셈(음수)에 대한 처리 수행.
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:  # op == '//'
        # 문제에서 음수 나눗셈은 C++14 기준으로 처리
        if a < 0:
            return -((-a) // b)
        else:
            return a // b

def dfs(index, current_value, plus_cnt, minus_cnt, mul_cnt, div_cnt):
    """
    index: 현재까지 사용한 수의 개수 (다음에 쓸 숫자는 sequence[index])
    current_value: 지금까지 계산된 결과
    plus_cnt, minus_cnt, mul_cnt, div_cnt: 남아있는 각 연산자의 개수
    """
    global maximum, minimum

    # 모든 수를 다 사용했다면(연산자를 N-1개 전부 사용) 최대/최소 갱신
    if index == N:
        maximum = max(maximum, current_value)
        minimum = min(minimum, current_value)
        return

    # 각 연산자가 남아있다면 사용
    if plus_cnt > 0:
        dfs(index + 1,
            calc('+', current_value, sequence[index]),
            plus_cnt - 1, minus_cnt, mul_cnt, div_cnt)

    if minus_cnt > 0:
        dfs(index + 1,
            calc('-', current_value, sequence[index]),
            plus_cnt, minus_cnt - 1, mul_cnt, div_cnt)

    if mul_cnt > 0:
        dfs(index + 1,
            calc('*', current_value, sequence[index]),
            plus_cnt, minus_cnt, mul_cnt - 1, div_cnt)

    if div_cnt > 0:
        dfs(index + 1,
            calc('//', current_value, sequence[index]),
            plus_cnt, minus_cnt, mul_cnt, div_cnt - 1)


# --- 메인 로직 ---
N = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().split()))
plus, minus, mul, div = map(int, sys.stdin.readline().split())

maximum = -10**10
minimum = 10**10

# 초깃값: 첫 번째 수를 결과로 삼고, index=1(두 번째 수부터 계산)
dfs(index=1,
    current_value=sequence[0],
    plus_cnt=plus, minus_cnt=minus, mul_cnt=mul, div_cnt=div)

print(maximum)
print(minimum)
