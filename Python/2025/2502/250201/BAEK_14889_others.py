import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
sum_stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
allstat = sum(sum_stat) // 2
result = 20000
for l in combinations(sum_stat, n//2):
    result = min(result, abs(allstat - sum(l)))
print(result)