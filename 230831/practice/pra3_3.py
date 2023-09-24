def subset(i, N, s, c):    # 이전까지 결정된 부분집합의 합
    if s == 0 and c != 0:   # 공집합일 때, 합이 0이 되므로 이 조건은 제외(c==0은 공집합인 상태)
        return 1
    elif i == N:
        return 0
    else:
        if subset(i+1, N, s+arr[i], c+1):
            return 1
        if subset(i+1, N, s, c):
            return 1
        return 0


# arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
arr = [1, 2, 3]
N = len(arr)
print(subset(0, N, 0, 0))
