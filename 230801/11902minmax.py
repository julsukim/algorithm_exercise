T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0 # 최솟값의 인덱스
    max_idx = 0 # 최대값의 인덱스
    for i in range(1, N):
        if arr[min_idx] > arr[i]: # 제일 왼쪽 택하기 (>)
            min_idx = i
        if arr[max_idx] <= arr[i]: # 제일 오른쪽 택하기 (<=)
            max_idx = i
    # if max_idx > min_idx:
    #     ans = max_idx - min_idx
    ans2 = max_idx - min_idx
    if ans2 < 0:
        ans2 = ans2 * -1

    print(ans2)