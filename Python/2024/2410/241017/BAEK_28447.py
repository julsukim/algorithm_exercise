from itertools import combinations
import sys
input = sys.stdin.readline


def recur(total, num, cnt):
    global result

    if num == N:
        if cnt == K:
            result = max(result, get_taste(total))
            return
        return

    total.append(num)
    recur(total, num + 1, cnt + 1)
    total.pop()
    recur(total, num + 1, cnt)


def get_taste(arr):
    if len(arr) == 0:
        return 0

    current_taste = 0

    combi = list(combinations(arr, 2))
    for a, b in combi:
        current_taste += ingredients[a][b]

    return current_taste


N, K = map(int, input().split())
ingredients = []
for i in range(N):
    ingredients.append(list(map(int, input().split())))

result = -99999999999999999

# combi = list(combinations(range(N), K))
# for comb in combi:
#     curr = 0
#     comps = list(combinations(comb, 2))
#     for a, b in comps:
#         curr += ingredients[a][b]
#     result = max(result, curr)

recur([], 0, 0)
print(result)
