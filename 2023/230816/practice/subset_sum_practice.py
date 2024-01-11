def f(i, N, s):    # s : i-1원소까지 고려한 부분집합의 합(포함된 원소의 합)
    global cnt
    cnt += 1
    if i==N:
        if s==10:
            print(bit)
        return
    else:
        bit[i] = 1    # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i])
        bit[i] = 0    # 부분집합에 A[i] 빠짐
        f(i+1, N, s)
        return

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N+1)]
bit = [0] * N
cnt = 0
f(0, N, 0)
print(cnt)