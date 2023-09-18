N = int(input())

num = (N-1)/3
i = 0
j = 1
while num > i*j:
    i += 1
    j += 1

print(j)