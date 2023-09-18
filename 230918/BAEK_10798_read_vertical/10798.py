arr = [list(input()) for _ in range(5)]
result = ''
for j in range(15):
    for i in range(5):
        try:
            result += arr[i][j]
        except:
            pass

print(result)
