N, M = map(int, input().split())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

# arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)
print(N, M)