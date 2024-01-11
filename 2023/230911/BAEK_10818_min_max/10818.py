N = int(input())
arr = list(map(int, input().split()))

# print(min(arr), max(arr))
minimum = 1000001
maximum = -1000001
for i in range(N):
    if maximum < arr[i]:
        maximum = arr[i]
    if minimum > arr[i]:
        minimum = arr[i]

print(minimum, maximum)
