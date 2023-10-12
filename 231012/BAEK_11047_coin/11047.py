N, K = map(int, input().split())
a = list(int(input()) for _ in range(N))

c = 0
s = 0
for i in range(N-1, -1, -1):
    if s == K:
        break
    if s + a[i] > K:
        continue
    else:
        c += (K-s)//a[i]
        s += a[i]*((K-s)//a[i])

print(c)
