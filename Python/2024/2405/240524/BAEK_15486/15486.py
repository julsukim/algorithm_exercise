import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]
dp = [-1]*(N+1)


def find_max_benefit(day):
    if day == N:
        return 0
    if dp[day] != -1:
        return dp[day]
    if day + schedules[day][0] > N:
        dp[day] = find_max_benefit(day + 1)
        return dp[day]
    tmp = max(find_max_benefit(day+1), find_max_benefit(day + schedules[day][0]) + schedules[day][1])
    dp[day] = tmp
    return tmp


print(find_max_benefit(0))
