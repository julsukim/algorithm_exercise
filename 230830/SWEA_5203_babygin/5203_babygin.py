import sys
sys.stdin =open('input.txt')


def is_baby_gin(arr):
    c1 = True
    c2 = True
    for i in range(2):
        if arr[i]+1 != arr[i+1]:
            c1 = False
        if arr[i] != arr[i+1]:
            c2 = False
    return (c1 == True) or (c2 == True)


def baby_gin(i, N, K, arr):
    global count
    if count >= 1:
        return
    elif i == K:
        result = is_baby_gin(p)
        if result == True:
            count += 1
            return
        else:
            return
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = arr[j]
                used[j] = 1
                baby_gin(i+1, N, K, arr)
                used[j] = 0


T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    player1 = []
    player2 = []

    print(f'#{tc}', end=' ')
    for i in range(12):
        if i % 2 == 0:
            player1.append(nums[i])
            N = len(player1)
            if N >= 3:
                used = [0] * N
                p = [0] * 3
                count = 0
                baby_gin(0, N, 3, player1)
                if count >= 1:
                    print(1)
                    break
        else:
            player2.append(nums[i])
            M = len(player2)
            if M >= 3:
                used = [0] * M
                p = [0] * 3
                count = 0
                baby_gin(0, M, 3, player2)
                if count >= 1:
                    print(2)
                    break
    else:
        print(0)