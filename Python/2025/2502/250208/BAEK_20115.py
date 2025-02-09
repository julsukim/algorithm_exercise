import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))

drinks.sort(reverse=True)
result = drinks[0]
for i in range(1, n):
    result += drinks[i] / 2
print(result)
# max_drink = max(drinks)
# sum_other = sum(drinks) - max_drink
#
# result = max_drink + sum_other / 2
# print(result)

