import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for num in arr:
        if num >= mid:
            tmp += num - mid
    if tmp == M:
        end = mid
        break
    elif tmp > M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
