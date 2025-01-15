# 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
# 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램

# N = int(input())
# glasses = [int(input()) for _ in range(N)]
#
#
# def recur(i, continuous, total):
#     global result
#     if i == N-1:
#         result = max(result, total)
#         return
#     if continuous == 0 or continuous == 1:
#         recur(i+1, continuous + 1, total + glasses[i])
#         recur(i+1, continuous, total)
#     elif continuous >= 2:
#         recur(i+1, 0, total)
#
#
# result = 0
# recur(0, 0, 0)
# print(result)

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
#
# N = int(input())
# glasses = [int(input()) for _ in range(N)]
#
# # 메모 딕셔너리: key = (i, continuous), value = 해당 상태에서의 최대 포도주 양
# memo = {}
#
#
# def recur(i, continuous):
#     # i가 N을 넘어가면(잔을 모두 고려했다면) 마실 수 있는 포도주가 없음
#     if i >= N:
#         return 0
#
#     # 이미 계산된 상태라면 memo에서 불러옴
#     if (i, continuous) in memo:
#         return memo[(i, continuous)]
#
#     # 만약 이미 2연속으로 마셨다면 이번 잔은 건너뛰기만 가능
#     if continuous == 2:
#         result = recur(i + 1, 0)
#     else:
#         # 현재 잔을 마시지 않는 경우
#         skip = recur(i + 1, 0)
#         # 현재 잔을 마시는 경우
#         drink = glasses[i] + recur(i + 1, continuous + 1)
#         # 두 경우 중 최댓값
#         result = max(skip, drink)
#
#     # 메모에 저장
#     memo[(i, continuous)] = result
#     return result
#
#
# recur(0, 0)
# print(memo[(0, 0)])

N = int(input())
glasses = [int(input()) for _ in range(N)]

# dp[i][c] = i번째 잔부터 끝까지 고려했을 때,
#            연속 c잔을 이미 마셨을 때 얻을 수 있는 최대 포도주 양
# 아직 계산되지 않은 상태는 -1로 초기화
dp = [[-1] * 3 for _ in range(N + 1)]


def recur(i, continuous):
    # 잔을 모두 고려한 경우
    if i >= N:
        return 0

    # 이미 계산된 상태라면 그 값을 바로 리턴
    if dp[i][continuous] != -1:
        return dp[i][continuous]

    # 2잔 연속 마신 상태라면, 이번 잔은 건너뛰어야 함
    if continuous == 2:
        dp[i][continuous] = recur(i + 1, 0)
    else:
        # 현재 잔을 건너뛰는 경우
        skip = recur(i + 1, 0)
        # 현재 잔을 마시는 경우
        drink = glasses[i] + recur(i + 1, continuous + 1)
        # 두 경우의 최댓값
        dp[i][continuous] = max(skip, drink)

    return dp[i][continuous]


print(recur(0, 0))
