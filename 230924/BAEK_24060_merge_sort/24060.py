import sys
input = sys.stdin.readline


def merge(left, right):
    global count
    result = [0] * (len(left) + len(right))
    idx = 0
    l_idx = 0   # left 리스트 인덱스
    r_idx = 0   # right 리스트 인덱스

    while l_idx < len(left) and r_idx < len(right):
        # left, right 인덱스의 값을 비교, 작은 값을 result에 넣기
        if left[l_idx] > right[r_idx]:
            result[idx] = right[r_idx]
            ans.append(right[r_idx])
            count += 1
            r_idx += 1
        else:
            result[idx] = left[l_idx]
            ans.append(left[l_idx])
            count += 1
            l_idx += 1
        idx += 1

    while l_idx < len(left):    # left가 아직 남은 상태
        result[idx] = left[l_idx]
        ans.append(left[l_idx])
        count += 1
        l_idx += 1
        idx += 1

    while r_idx < len(right):   # right가 남은 상태
        result[idx] = right[r_idx]
        ans.append(right[r_idx])
        count += 1
        r_idx += 1
        idx += 1

    return result


# 분할
def merge_sort(arr):
    # 절반 씩 나누어서 분할
    # 최소 단위일 때 return
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # print(left, right)
    # 합치는 부분을 추가
    return merge(left, right)


N, K = map(int, input().split())
A = list(map(int, input().split()))
tmp = [0]*N
ans = []
count = 0
merge_sort(A)
if count < K:
    print(-1)
else:
    print(ans[K-1])
