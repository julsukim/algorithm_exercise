import sys
sys.stdin = open('input.txt')

def special_array(arr):
    for i in range(0, len(arr)):
        min_idx = i
        max_idx = i
        if i % 2 != 1:
            for j in range(i + 1, len(arr)):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            for k in range(i + 1, len(arr)):
                if arr[min_idx] > arr[k]:
                    min_idx = k
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    result = special_array(num_list)[:10]

    print(f'#{tc}', end=' ')
    for i in result:
        print(i, end=' ')
    print()