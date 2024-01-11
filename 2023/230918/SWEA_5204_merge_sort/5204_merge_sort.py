import sys
sys.stdin = open('input.txt')


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = []
    right = []
    middle = len(arr) // 2
    for p in range(middle):
        left.append(arr[p])
    for q in range(middle, len(arr)):
        right.append(arr[q])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global count
    result = []

    i = 0
    j = 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left):
            if i == len(left) - 1:
                print(left, right)
                count += 1
            result.append(left[i])
            i += 1
        elif j < len(right):
            result.append(right[j])
            j += 1

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    result = merge_sort(arr)
    print(f'#{tc} {result[N//2]} {count}')
