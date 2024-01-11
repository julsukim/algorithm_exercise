def is_sosu(n):
    global cnt
    if 1 < n < 4:
        cnt += 1
        return
    else:
        for i in range(2, (n-1)):
            if n % i == 0:
                break
        else:
            cnt += 1
            return


N = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in arr:
    if i == 1:
        continue
    else:
        is_sosu(i)
print(cnt)