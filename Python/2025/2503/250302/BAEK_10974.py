from itertools import permutations

N = int(input())
nums = list(range(1, N+1))

perms = list(permutations(nums))
result = []
for perm in perms:
    result.append(' '.join(map(str, perm)))
print('\n'.join(result))
