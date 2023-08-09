import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * (N+2)
    arr[1] = 1
    pre_arr = arr

    print(f'#{tc}')
    for i in range(1, N + 1):
        pre_arr = arr.copy()
        for j in range(1, i+1):
            arr[j] = pre_arr[j-1] + pre_arr[j]
        for k in arr:
            if k != 0:
                print(k, end=' ')
        print()
