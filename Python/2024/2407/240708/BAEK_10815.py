import sys
input = sys.stdin.readline


N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()
for num in arr2:
    start = 0
    end = N-1
    flag = False

    while start <= end:
        mid = (end + start) // 2

        if arr1[mid] == num:
            flag = True
            break

        elif arr1[mid] > num:
            end = mid - 1

        else:
            start = mid + 1

    if flag:
        print(1, end=' ')
    else:
        print(0, end=' ')
