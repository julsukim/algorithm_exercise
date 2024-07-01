import sys
sys.stdin = open('input.txt')

delta = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]

    xs = []
    ys = []
    for i in range(N):
        x = atoms[i][0]
        y = atoms[i][1]
        xs.append(x)
        ys.append(y)

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    e = 0
    while len(atoms) >= 2:
        for atom in atoms:
            atom[0] += delta[atom[2]][0]
            atom[1] += delta[atom[2]][1]

        collide = {}
        for atom in atoms:
            try:
                collide[(atom[0], atom[1])].append(atom)
            except KeyError:
                collide[(atom[0], atom[1])] = [atom]

        atoms = []
        for v in collide:
            if len(collide[v]) >= 2:
                for a in collide[v]:
                    e += a[3]
            else:
                if min_x<=collide[v][0][0]<=max_x and min_y<=collide[v][0][1]<=max_y:
                    atoms.append(collide[v][0])
    print(f'#{tc} {e}')