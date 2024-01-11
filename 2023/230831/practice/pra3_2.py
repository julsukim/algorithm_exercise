def subset(i, N, s):    # 이전까지 결정된 부분집합의 합
    if s == 0:
        return 1
    elif i == N:
        return 0
    else:
        if subset(i+1, N, s+arr[i]):
            return 1
        if subset(i+1, N, s):
            return 1
        return 0
    return


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# arr = [1, 2, 3] # 공집합일 때, 공집합은 s==0이므로 1이 리턴되는 문제.
N = len(arr)
print(subset(0, N, 0))
