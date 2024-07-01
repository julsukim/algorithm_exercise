import sys
sys.stdin = open('input.txt')


def f(i, N, c, s):      # 시작, 원소개수, 부분집합 내 원소의 개수, 부분집합 내 원소의 합
    if c == 7 and s == 100:     # 부분집합의 개수, 합이 7, 100
        tmp = []
        for i in range(9):
            if bit[i] == 1:
                tmp.append(dwarfs[i])
        result.append(tmp)
        return
    elif i == N:
        return
    elif s > 100:
        return
    elif c > 7:
        return
    else:
        bit[i] = 1
        c+=1
        f(i+1, N, c, s+dwarfs[i])
        bit[i] = 0
        c-=1
        f(i+1, N, c, s)
        return


dwarfs = [] + [int(input()) for _ in range(9)]
dwarfs.sort()
bit = [0] * 9
result = []
f(0, 9, 0, 0)

for i in range(1):
    for j in range(7):
        print(result[i][j])