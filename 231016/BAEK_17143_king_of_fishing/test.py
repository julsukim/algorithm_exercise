C = 4
arr = list(range(1, C+1))
arr2 = list(range(C-1, 0, -1))
arr.extend(arr2)
print(arr)
col = 2
speed = 8

print(arr[arr.index(col)+(speed%C)])
