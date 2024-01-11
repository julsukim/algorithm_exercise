import sys
sys.stdin = open('input.txt')

N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]

dp = [[0, 0] for _ in range(N+1)]
dp[N][1] = stairs[N]

if len(stairs) == 2:
    print(stairs[N])
elif len(stairs) == 3:
    print(stairs[1]+stairs[2])
elif len(stairs) == 4:
    print(max(stairs[2]+stairs[3], stairs[1]+stairs[3]))
else:
    dp[N-1][0] = stairs[N-1] + stairs[N]
    dp[N-1][1] = stairs[N]

    dp[N-2][0] = stairs[N-2] + stairs[N]
    dp[N-2][1] = stairs[N-2] + stairs[N]

    for i in range(N-3, -1, -1):
        dp[i][0] = max(dp[i+2][0], dp[i+2][1]) + stairs[i]
        dp[i][1] = dp[i+1][0] + stairs[i]

    case = [dp[0][0], dp[0][1], dp[1][0], dp[1][1]]
    print(max(case))
print(dp)