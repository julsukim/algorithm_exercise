N = 9

arr = [list(map(int, input().split())) for _ in range(N)]
maximum = 0
max_loc = [0, 0]
for i in range(N):
    for j in range(N):
        if maximum <= arr[i][j]:
            maximum = arr[i][j]
            max_loc = [i+1, j+1]

print(maximum)
print(*max_loc)
