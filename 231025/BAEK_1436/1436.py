N = int(input())
arr = []

for i in range(5000000):
    if '666' in str(i):
        arr.append(i)
print(arr[N-1])
