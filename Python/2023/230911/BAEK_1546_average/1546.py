N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
new_total = 0
for score in scores:
    new_total += (score/M) * 100
print(new_total/N)
