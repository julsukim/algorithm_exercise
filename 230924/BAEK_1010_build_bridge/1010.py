def factorial(n, ans):
    if n == 0:
        result.append(ans)
        return
    ans *= n
    factorial(n-1, ans)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    result = []
    factorial(M, 1)
    factorial(N, 1)
    factorial(M-N, 1)
    print(result[0]//result[1]//result[2])
