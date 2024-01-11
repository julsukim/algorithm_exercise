N, M = map(int, input().split())
arr = list(range(0, (N+1)))
for _ in range(M):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]

for k in range(1, (N+1)):
    print(arr[k], end=' ')
