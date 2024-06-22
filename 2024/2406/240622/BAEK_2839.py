# 3kg, 5kg
# 최소

N = int(input())
count = 0
tmp = N
count += tmp // 5
tmp %= 5
count3 = 0
if tmp == 0:
    print(count)
else:
    if tmp % 3 == 0:
        count3 += tmp // 3
        print(count+count3)
    else:
        while True:
            count -= 1
            tmp += 5
            if tmp > N:
                print(-1)
                break
            if tmp % 3 == 0:
                count3 += tmp // 3
                print(count+count3)
                break
