# 이 문제는 "다중 배낭 문제" (Multiple Knapsack Problem)로,
# 각 보급품을 여러 배낭에 나눠 담을 수 없는 상황을 다룹니다.
# 이를 해결하기 위해서는 다음과 같은 접근 방식이 필요합니다:
#
# 보급품의 가치를 기준으로 정렬합니다.
# 각 신입사원에게 배낭을 채우기 위해 동적 프로그래밍을 사용합니다.
# 각 신입사원마다 남은 보급품을 이용하여 최대 가치를 찾아서 배낭을 채웁니다.


def knapsack(N, M, items, taken):
    # DP 테이블 초기화
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        weight, value = items[i - 1]
        for w in range(M + 1):
            if weight <= w and not taken[i - 1]:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    # 최대 가치를 찾고, 선택된 아이템을 표시
    max_value = dp[N][M]
    w = M
    for i in range(N, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            taken[i - 1] = True
            w -= items[i - 1][0]

    return max_value


def max_total_value(N, K, M, items):
    # 보급품을 가치 대비 무게 비율로 정렬
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    taken = [False] * N

    total_value = 0
    for _ in range(K):
        total_value += knapsack(N, M, items, taken)

    return total_value


# 입력 예시
N = 5
K = 2
M = 5
items = [(4, 5), (3, 4), (2, 1), (5, 7), (1, 1)]

# 최대 가치 계산
result = max_total_value(N, K, M, items)
print(result)  # 결과 출력
