N, M = map(int, input().split())
numbers = [0] * (N+1)
for i in range(1, N+1):
    numbers[i] = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(min(numbers[a:b+1]), max(numbers[a:b+1]))
# 모르겠당 너무 어려워용