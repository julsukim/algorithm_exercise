import time


def ncr(n, r):
    if r == 0:
        print(tr)
    elif n < r:     # 남은 원소보다 많은 원소를 선택해야하는 경우
        return      # 불가
    else:
        tr[r-1] = A[n-1]    # a[n-1] 조합에 포함시키는 경우
        ncr(n-1, r-1)
        ncr(n-1, r)         # a[n-1]을 포함시키지 않는 경우


start = time.time()
R = 5
A = list(range(1, 21))
N = len(A)
tr = [0] * R
ncr(N, R)
end = time.time()

print(f"{end - start:.6f} sec")
