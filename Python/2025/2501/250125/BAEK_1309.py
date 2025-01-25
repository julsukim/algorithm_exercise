# N = int(input())
# if N == 1:
#     print(3)
# elif N == 2:
#     print(7)
# elif N == 3:
#     print(17)
# else:
#     dp = [0]*(N+1)
#     dp[0] = 1
#     dp[1] = 3
#     dp[2] = 7
#     dp[3] = 17
#     for i in range(4, N+1):
#         dp[i] = (dp[i-2] * 3 + (dp[i-1] - dp[i-2]) * 2) % 9901
#     print(dp[N] % 9901)


N = int(input().strip())
# dp[i][0] = i번째 열에 사자를 놓지 않은 경우
# dp[i][1] = i번째 열에 윗칸만 사자를 놓은 경우
# dp[i][2] = i번째 열에 아랫칸만 사자를 놓은 경우
dp = [[0]*3 for _ in range(N+1)]

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

result = sum(dp[N]) % 9901
print(result)



# def recur(i, t, last):
#     global total
#     if i >= t:
#         total += 1
#         return
#
#     if last == 'none':
#         recur(i+1, t, 'none')
#         recur(i+1, t, 'left')
#         recur(i+1, t, 'right')
#     elif last == 'left':
#         recur(i+1, t, 'none')
#         recur(i+1, t, 'right')
#     elif last == 'right':
#         recur(i+1, t, 'none')
#         recur(i+1, t, 'left')
#
#
# result = [0] * N
# result[0] = 1
# for i in range(1, N):
#     total = 0
#     recur(0, i, 'none')
#     result[i] = total
# print(result)
