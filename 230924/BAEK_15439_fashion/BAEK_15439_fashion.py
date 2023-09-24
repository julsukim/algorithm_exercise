N = int(input())
R = 2
cnt = 0
if N < R:
    print(0)
else:
    cnt += N*(N-1)
    print(cnt)
