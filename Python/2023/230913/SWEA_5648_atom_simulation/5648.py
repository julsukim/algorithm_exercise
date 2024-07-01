import sys
sys.stdin= open('input.txt')

# 0: 상, 1: 하, 2: 좌, 3: 우
dx = {0: 0, 1: 0, 2: -0.5, 3: 0.5}
dy = {0: 0.5, 1: -0.5, 2: 0, 3: 0}

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    e = 0
    while len(atoms) >= 2:
        for atom in atoms:
            atom[0] += dx[atom[2]]
            atom[1] += dy[atom[2]]

        coordinates = {}
        for atom in atoms:
            try:
                coordinates[(atom[0], atom[1])].append(atom)
            except KeyError:
                coordinates[(atom[0], atom[1])] = [atom]

        atoms = []
        for coord in coordinates:
            if len(coordinates[coord]) >= 2:
                for i in coordinates[coord]:
                    e += i[3]
            else:
                if -1000 <= coordinates[coord][0][0] <= 1000 and -1000 <= coordinates[coord][0][1] <= 1000:
                    atoms.append(coordinates[coord][0])

    print(f'#{tc} {e}')