import sys
sys.stdin = open('input.txt')


def is_baby_gin(arr):
    case1 = arr[:3]
    case2 = arr[3:]
    c1 = True
    c2 = True
    c3 = True
    c4 = True
    for i in range(2):
        if case1[i]+1 != case1[i+1]:
            c1 = False
    for j in range(2):
        if case1[j] != case1[j+1]:
            c2 = False
    for k in range(2):
        if case2[k]+1 != case2[k+1]:
            c3 = False
    for l in range(2):
        if case2[l] != case2[l+1]:
            c4 = False
    return (c1 == True or c2 == True) and (c3 == True or c4 == True)


def baby_gin(i, N, K):
    global count
    if count > 1:
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
                p[i] = numbers[j]
                used[j] = 1
                baby_gin(i+1, N, K)
                used[j] = 0


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().strip()))
    N = len(numbers)
    K = 6
    used = [0] * N
    p = [0] * K

    count = 0
    baby_gin(0, N, K)
    if count > 0:
        count = 1

    print(f'#{tc} {count}')
