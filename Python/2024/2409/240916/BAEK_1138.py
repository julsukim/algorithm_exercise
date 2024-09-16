N = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(N, 0, -1):
    pos = arr[i - 1]
    result.insert(pos, i)

print(" ".join(map(str, result)))
