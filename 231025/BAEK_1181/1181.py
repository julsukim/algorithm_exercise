N = int(input())
arr = [input() for _ in range(N)]
arr2 = list(set(arr))
arr2.sort(key=lambda x: (len(x), x))
for e in arr2:
    print(e)
