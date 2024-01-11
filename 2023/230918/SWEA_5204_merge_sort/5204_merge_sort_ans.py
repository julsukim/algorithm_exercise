import sys
sys.stdin = open('input.txt')


def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    idx = 0
    l_idx = 0   # left 리스트 인덱스
    r_idx = 0   # right 리스트 인덱스

    while l_idx < len(left) and r_idx < len(right):
        # left, right 인덱스의 값을 비교, 작은 값을 result에 넣기
        if left[l_idx] > right[r_idx]:
            result[idx] = right[r_idx]
            r_idx += 1
        else:
            result[idx] = left[l_idx]
            l_idx += 1
        idx += 1

    while l_idx < len(left):    # left가 아직 남은 상태
        result[idx] = left[l_idx]
        l_idx += 1
        idx += 1

    while r_idx < len(right):   # right가 남은 상태
        result[idx] = right[r_idx]
        r_idx += 1
        idx += 1

    if left[-1] > right[-1]:
        cnt += 1

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


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    res = merge_sort(arr)
    print(f'#{tc} {res[N//2]} {cnt}')