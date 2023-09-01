def work(i, s, arr):
    global cnt
    if i == N:
        if s == T:
            arr.append(1)
    else:
        work(i + 1, s + numbers[i], arr)
        work(i + 1, s - numbers[i], arr)


numbers = [4, 1, 2, 1]
T = 4
N = len(numbers)
arr = []

cnt = 0
work(0, 0, arr)
print(arr)