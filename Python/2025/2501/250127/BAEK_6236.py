N, M = map(int, input().split())
expenses = [int(input()) for _ in range(N)]
# N일 동안 사용할 금액
# M번만 통장에서 돈을 뺀다.
# 통장에서 K원을 인출 -> 사용 / 모자라면 남은 금액 넣고 다시 인출
# 남은 금액이 많더라도 다시 인출 가능

# left(최솟값)은 최소한 하루 치 지출을 감당할 수 있어야 한다.
left = max(expenses)
# right(최댓값)은 모든 지출을 한 번에 지출할 수 있어야 한다.
right = sum(expenses)
result = right

while left <= right:
    mid = (left + right) // 2
    current = mid
    cnt = 1

    for i in range(N):
        if current - expenses[i] >= 0:
            current -= expenses[i]
        else:
            current = mid - expenses[i]
            cnt += 1

    if cnt <= M:
        result = mid
        right = mid - 1
    elif cnt > M:
        left = mid + 1


print(result)
