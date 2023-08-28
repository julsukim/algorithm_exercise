import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_cnt = 1
    cnt = 1
    for i in range(1, N):
        if arr[i-1] <= arr[i]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 1

    for i in range(1, N):
        if arr[i - 1] >= arr[i]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt

    print(max_cnt)