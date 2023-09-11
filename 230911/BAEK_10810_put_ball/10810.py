N, M = map(int, input().split())
list = [0] * (N+1)
for _ in range(M):
    i, j, k = map(int, input().split())
    for p in range(i, j+1):
        list[p] = k

for q in range(1, N+1):
    print(list[q], end=' ')
