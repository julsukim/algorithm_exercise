arr = [69, 10, 30, 2, 16, 8, 31, 22]


def merge_sort(arr):
    if len(arr) == 1 :
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
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result


print(merge_sort(arr))