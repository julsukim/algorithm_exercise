import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    nums, M = input().split()
    board = list(nums)
    M = int(M)
    N = len(board)

    high = []
    low = []
    mini = 11
    maxi = 0
    for i in range(N):
        if maxi <= board[i]:
            maxi = board[i]
            high.append(i)
