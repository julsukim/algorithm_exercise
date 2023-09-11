N = int(input())
numbers = list(map(int, input().split()))
v = int(input())

# cnt = 0
# for i in range(N):
#     if numbers[i] == v:
#         cnt += 1
# print(cnt)

cnt = numbers.count(v)
print(cnt)