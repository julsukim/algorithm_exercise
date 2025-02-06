import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

increments = list(map(int, input().split()))
case = 0


def recur(day, weight, used):
    global case
    if day >= N:
        if weight >= 500:
            case += 1
        return

    weight -= K

    for i in range(N):
        if not used[i] and (weight + increments[i]) >= 500:
            used[i] = True
            recur(day+1, weight + increments[i], used)
            used[i] = False


recur(0, 500, [False] * N)
print(case)
