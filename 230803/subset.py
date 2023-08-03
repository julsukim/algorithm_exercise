arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]

def print_subset(bit, arr, n):
    total = 0 # 부분집합의 합
    for i in range(n):
        if bit[i]:
            print(arr[i], end = ' ')
            total += arr[i]
    print(bit, total)

ans = 0

for i in range(2):
    bit[0] = i # 0번 원소
    for j in range(2):
        bit[1] = j # 1번 원소
        for k in range(2):
            bit[2] = k # 2번 원소
            for l in range(2):
                bit[3] = l # 3번 원소
                print_subset(bit, arr, 4) # 생성된 부분집합 출력
                if total > 1:
                    ans = 1