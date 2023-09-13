import sys
sys.stdin= open('input.txt')

# 0: 상, 1: 하, 2: 좌, 3: 우

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    e = 0
    while cnt <= 2000:
        for atom in atoms:
            if atom[2] == 0:
                atom[1] += 1
            elif atom[2] == 1:
                atom[1] -= 1
            elif atom[2] == 2:
                atom[0] -= 1
            else:
                atom[0] += 1
        for i in range(N-1):
            for j in range(i+1, N):
                if atoms[i][0] == atoms[j][0] and atoms[i][1] == atoms[j][1]:
                    e += atoms[i][3] + atoms[j][3]
                    atoms[i][3] = atoms[j][3] = 0
        cnt += 1
        rest = 0
        for i in range(N):
            if atoms[i][3] != 0:
                rest += 1
        if rest <= 1:
            break

    print(f'#{tc} {e}')