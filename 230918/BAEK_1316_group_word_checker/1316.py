N = int(input())
count = 0
for _ in range(N):
    word = input()
    checker = []
    for i in word:
        if i not in checker:
            checker.append(i)
        elif i == checker[-1]:
            continue
        else:
            break
    else:
        count += 1

print(count)
