def factorial(n, ans):
    if n == 0:
        result.append(ans)
        return
    ans *= n
    factorial(n-1, ans)


N, K = map(int, input().split())
result = []
factorial(N, 1)
factorial(K, 1)
factorial(N - K, 1)
print(result[0]//result[1]//result[2])
