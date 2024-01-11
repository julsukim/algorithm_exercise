import time


def nCr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)


start = time.time()
A = list(range(1, 21))
N = len(A)
R = 5
comb = [0] * R
nCr(N, R, 0)
end = time.time()

print(f"{end - start:.6f} sec")
