from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

combs = list(combinations(arr, 3))
best_sum = 0

for comb in combs:
    current_sum = sum(comb)
    if best_sum < current_sum <= M:
        best_sum = current_sum

print(best_sum)
