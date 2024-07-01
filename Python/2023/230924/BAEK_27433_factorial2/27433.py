def factorial(n):
    global result
    if n == 0:
        print(result)
        return
    result *= n
    factorial(n-1)


N = int(input())
result = 1
factorial(N)
