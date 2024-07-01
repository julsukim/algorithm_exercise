def f(arr, arr2):
    stack = []
    visited = [0] * (N+1)
    v = arr[0]
    visited[v] = 1
    for k in arr2:
        visited[k] = 1
    while True:
        is_find = False
        for w in range(1, len(info[v])):
            if visited[info[v][w]] == 0:
                stack.append(v)
                v = info[v][w]
                visited[v] = 1
                is_find = True
                break
        if is_find == False:
            if len(stack) != 0:
                v = stack.pop()
            else:
                break

    result = True
    for i in arr:
        if visited[i] == 0:
            result = False

    return result


N = int(input())
population = list(map(int, input().split()))

info = [[]]
for _ in range(N):
    info.append(list(map(int, input().split())))
areas = list(range(1, N + 1))

min_v = 1000
for i in range(1, (1 << N) // 2):
    group1 = []
    group2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i & (1 << j):
            group1.append(areas[j])
            total1 += population[j]
        else:
            group2.append(areas[j])
            total2 += population[j]
    r1 = f(group1, group2)
    r2 = f(group2, group1)
    if r1 == True and r2 == True:
        if min_v > abs(total1 - total2):
            min_v = abs(total1 - total2)
if min_v == 1000:
    min_v = -1

print(min_v)
