import sys
sys.stdin = open('input.txt')


def binarySearch(l, r, target, is_l, is_r):
    if l > r:
        return False

    m = (l+r) // 2
    if A[m] == target:
        if m == (N-1)//2:
            return True
        elif is_r == False and is_l == False:
            return False
        else:
            return True
    elif A[m] < target:
        if is_r == True:
            return False
        else:
            is_l = False
            is_r = True
            return binarySearch(m+1, r, target, is_l, is_r)
    else:
        if is_l == True:
            return False
        else:
            is_r = False
            is_l = True
            return binarySearch(l, m-1, target, is_l, is_r)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()
    count = 0
    for i in B:
        is_l = False
        is_r = False
        if binarySearch(0, N-1, i, is_l, is_r) == True:
            count += 1

    print(f'#{tc} {count}')