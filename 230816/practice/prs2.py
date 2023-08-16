def f(i, N, s, t):    # t : 찾으려는 합
    global cnt
    cnt += 1
    if s == t:
        print(bit)
        return
    elif i == N:    # t는 아니지만, 남은 원소가 없는 경우
        return
    elif s > t:
        return
    else:
        bit[i] = 1    # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i], t)
        bit[i] = 0    # 부분집합에 A[i] 빠짐
        f(i+1, N, s, t)
        return

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N+1)]
bit = [0] * N
cnt = 0
f(0, N, 0, 10)
print(cnt)