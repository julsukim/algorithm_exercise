import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for num in arr:
        if num > mid:
            tmp += mid
        else:
            tmp += num

    if tmp == M:
        end = mid
        break
    elif tmp > M:
        end = mid - 1
    else:
        start = mid + 1

print(end)
