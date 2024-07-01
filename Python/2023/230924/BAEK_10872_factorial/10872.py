def factorial(n):
    global result
    if n == 0:
        return
    result *= n
    factorial(n-1)


N = int(input())
result = 1
factorial(N)
print(result)
