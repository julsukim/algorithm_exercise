import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for num in arr:
        tmp += num // mid

    if tmp >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
