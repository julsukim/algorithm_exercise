a = [3, 6, 7, 1, 5, 4]
N = 6

for i in range(1<<N):     # 1<<N == 2**N
    subset1 = []
    for j in range(N):
        if i&(1<<j):    # j번 비트가 0이 아니면
            subset1.append(a[j])
    print(*subset1)

# 그룹을 2개로 나누어서 부분집합 만들기
for i in range(1<<N):
    group1 = []
    group2 = []
    for j in range(N):
        if i&(1<<j):    # j번 비트가 0이 아니면
            group1.append(a[j])
        else:
            group2.append(a[j])
    print(group1, group2)

# 공집합은 제외하기
for i in range(1, (1<<N)-1):
    group1 = []
    group2 = []
    for j in range(N):
        if i&(1<<j):    # j번 비트가 0이 아니면
            group1.append(a[j])
        else:
            group2.append(a[j])
    print(group1, group2)

# 중복되는 그룹 제거
# for i in range(1, 1<<(N-1)):
for i in range(1, (1<<N)//2):
    group1 = []
    group2 = []
    for j in range(N):
        if i&(1<<j):    # j번 비트가 0이 아니면
            group1.append(a[j])
        else:
            group2.append(a[j])
    print(group1, group2)

# 응용하는 방법 예시
min_v = 1000
for i in range(1, (1<<N)//2):
    group1 = []
    group2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i&(1<<j):    # j번 비트가 0이 아니면
            group1.append(a[j])
            total1 += a[j]
        else:
            group2.append(a[j])
            total2 += a[j]
    r1 = f(group1)
    r2 = f(group2)
    if r1 and r2:
        if min_v > abs(total1 - total2):
            min_v = abs(total1 - total2)
    print(group1, group2)
