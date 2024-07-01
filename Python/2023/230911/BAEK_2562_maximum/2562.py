arr = [int(input()) for _ in range(9)]
M = max(arr)
print(M)
for i in range(len(arr)):
    if M == arr[i]:
        print(i+1)
