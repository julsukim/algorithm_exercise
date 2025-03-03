def power_of_three_count(x):
    count = 0
    while x > 1:
        x //= 3
        count += 1

    return count


def sol(n, si, sj):
    if n <= 0:
        return
    third = 3**(n-1)
    for i in range(si + third, si + third *2):
        for j in range(sj + third, sj + third *2):
            arr[i][j] = ' '

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            sol(n-1, si + third*i, sj + third*j)


N = int(input())
arr = [['*']*N for _ in range(N)]

sol(power_of_three_count(N), 0, 0)

for i in range(N):
    print(''.join(arr[i]))
