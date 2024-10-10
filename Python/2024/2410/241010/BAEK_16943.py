from itertools import permutations

A, B = map(int, input().split())

list_a = list(map(int, str(A)))
perm_a = list(permutations(list_a))

maximum = -1
for num_list in perm_a:
    if num_list[0] == 0:
        continue
    num = int(''.join(map(str, num_list)))
    if num < B:
        maximum = max(num, maximum)

print(maximum)
