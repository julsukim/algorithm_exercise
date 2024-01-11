import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    t = True # ascending / descending
    cnt = 1
    s = 1
    max_cnt = 1
    for i in range(1, N):
        if i == 1:
            if arr[i-1] < arr[i]:
                t = True
                cnt += 1
                s = 1
            elif arr[i-1] > arr[i]:
                t = False
                cnt += 1
                s = 1
            else:
                s += 1
                cnt += 1
        elif t == True and cnt > 1:
            if arr[i-1] < arr[i]:
                t = True
                cnt += 1
                s = 1
            elif arr[i-1] > arr[i]:
                if max_cnt < cnt:
                    max_cnt = cnt
                t = False
                cnt = s + 1
                s = 1
            else:
                s += 1
                cnt += 1
        elif t == False and cnt > 1:
            if arr[i-1] < arr[i]:
                if max_cnt < cnt:
                    max_cnt = cnt
                t = True
                cnt = s + 1
                s = 1
            elif arr[i-1] > arr[i]:
                t = False
                cnt += 1
                s = 1
            else:
                s += 1
                cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
    print(max_cnt)
