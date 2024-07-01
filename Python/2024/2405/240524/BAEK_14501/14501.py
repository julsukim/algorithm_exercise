import sys
sys.setrecursionlimit(100000)

N = int(input())
schedules = []
for i in range(N):
    end, profit = map(int, input().split())
    schedules.append([end, profit])
answer = 0
dp = [-1]*(N+1)


def find_max_benefit(day):
    global answer
    if day > N:
        return -1234352342
    if day == N:
        return 0
    if dp[day] != -1:
        return dp[day]
    else:
        tmp = -1235234234234

        for i in range(len(schedules)):
            if day == i:
                tmp = max(tmp, find_max_benefit(day + schedules[i][0]) + schedules[i][1])
                break
        tmp = max(tmp, find_max_benefit(day+1))
        dp[day] = tmp
        return tmp


answer = find_max_benefit(0)
print(answer)
