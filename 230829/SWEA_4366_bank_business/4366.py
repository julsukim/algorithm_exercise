import sys
sys.stdin = open('input.txt')


def dec_2(str):
    return int(str, 2)


def dec_3(str):
    num = 0
    for i in range(len(str)-1, -1, -1):
        num += int(str[i]) * (3**(len(str)-(i+1)))
    return num


T = int(input())
for tc in range(1, T+1):
    binary = list(input())
    ternary = list(input())
    N, M = len(binary), len(ternary)

    b = []
    t = []
    for i in range(N):
        tmp = binary.copy()
        if tmp[i] == '1':
            tmp[i] = '0'
        else:
            tmp[i] = '1'
        b.append(''.join(tmp))

    for j in range(M):
        tmp = ternary.copy()
        for k in range(3):
            if ternary[j] == str(k):
                continue
            else:
                tmp[j] = str(k)
                t.append((''.join(tmp.copy())).lstrip('0'))

    print(f'#{tc}', end=' ')
    for bi in b:
        for te in t:
            if dec_2(bi) == dec_3(te):
                print(dec_2(bi))