# M, N = map(int, input().split())
# sets = {2}
#
# for i in range(3, N+1):
#     flag = False
#     for j in sets:
#         mod = i % j
#         if mod == 0:
#             flag = True
#             break
#     if not flag:
#         sets.add(i)
#
# res = sorted([str(i) for i in sets if M <= i])
# print('\n'.join(res))

M, N = map(int, input().split())
sieve = [True] * (N + 1)
sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        for j in range(i * i, N + 1, i):
            sieve[j] = False

for i in range(M, N + 1):
    if sieve[i]:
        print(i)
