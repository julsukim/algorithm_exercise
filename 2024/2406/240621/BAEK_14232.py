K = int(input())
arr = []
for i in range(2, int(K**0.5)+1):
    while K % i == 0:
        arr.append(i)
        K = K // i
if K != 1:
    arr.append(K)
print(len(arr))
print(*arr)
