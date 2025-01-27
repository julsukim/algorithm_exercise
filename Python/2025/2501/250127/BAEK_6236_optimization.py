import sys
input = sys.stdin.readline

N, M = map(int, input().split())
expenses = [int(input()) for _ in range(N)]

left = max(expenses)
right = sum(expenses)
answer = right


def simulate(k):
    current = k
    cnt = 1

    for i in range(N):
        if current - expenses[i] >= 0:
            current -= expenses[i]
        else:
            current = mid - expenses[i]
            cnt += 1

    if cnt <= M:
        return True
    return False


while left <= right:
    mid = (left + right) // 2

    result = simulate(mid)

    if result:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1


print(answer)
