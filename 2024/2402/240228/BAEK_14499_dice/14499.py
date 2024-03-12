# 14499 주사위 굴리기
# 동 1, 서 2, 북 3, 남 4
# 상단에 쓰여있는 값 출력
# 지도 바깥으로 이동 -> 명령 무시, 출력 X
'''
N, M, r, c, K = map(int, input().split())
zido = []
for _ in range(N):
    zido.append(list(map(int, input().split())))
orders = list(map(int, input().split()))

delta = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]

hori = [0, 0, 0, 0]
vert = [0, 0, 0, 0]

h_top = 1
h_bottom = 3
v_top = 1
v_bottom = 3

for order in orders:

    if order == 1:
        dr, dc = delta[1]
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            r, c = nr, nc
            h_top = (h_top + 3) % 4
            h_bottom = (h_top + 2) % 4
            if zido[r][c] != 0:
                hori[h_bottom] = zido[r][c]
                zido[r][c] = 0
            else:
                zido[r][c] = hori[h_bottom]
            vert[v_top] = hori[h_top]
            vert[v_bottom] = hori[h_bottom]
            print("동", hori, vert, hori[h_top], hori[h_bottom], vert[v_top], vert[v_bottom])
            print(h_top, h_bottom, v_top, v_bottom)

    elif order == 2:
        dr, dc = delta[2]
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            r, c = nr, nc
            h_top = (h_top + 1) % 4
            h_bottom = (h_bottom + 2) % 4
            if zido[r][c] != 0:
                hori[h_bottom] = zido[r][c]
                zido[r][c] = 0
            else:
                zido[r][c] = hori[h_bottom]
            vert[v_top] = hori[h_top]
            vert[v_bottom] = hori[h_bottom]
            print("서", hori, vert, hori[h_top], hori[h_bottom], vert[v_top], vert[v_bottom])
            print(h_top, h_bottom, v_top, v_bottom)

    elif order == 3:
        dr, dc = delta[3]
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            r, c = nr, nc
            v_top = (v_top + 1) % 4
            v_bottom = (v_top + 2) % 4
            if zido[r][c] != 0:
                vert[v_bottom] = zido[r][c]
                zido[r][c] = 0
            else:
                zido[r][c] = vert[v_bottom]
            hori[h_top] = vert[v_top]
            hori[h_bottom] = vert[v_bottom]
            print("북", hori, vert, hori[h_top], hori[h_bottom], vert[v_top], vert[v_bottom])
            print(h_top, h_bottom, v_top, v_bottom)

    else:
        dr, dc = delta[4]
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            r, c = nr, nc
            v_top = (v_top + 3) % 4
            v_bottom = (v_top + 2) % 4
            if zido[r][c] != 0:
                vert[v_bottom] = zido[r][c]
                zido[r][c] = 0
            else:
                zido[r][c] = vert[v_bottom]
            hori[h_top] = vert[v_top]
            hori[h_bottom] = vert[v_bottom]
            print("남", hori, vert, hori[h_top], hori[h_bottom], vert[v_top], vert[v_bottom])
            print(h_top, h_bottom, v_top, v_bottom)
'''
N, M, r, c, K = map(int, input().split())
zido = []
for _ in range(N):
    zido.append(list(map(int, input().split())))
orders = list(map(int, input().split()))

delta = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]

hori = [0, 0, 0, 0]
vert = [0, 0, 0, 0]

h_top = 1
h_bottom = 3
v_top = 1
v_bottom = 3

for order in orders:

    if order == 1:
        nr, nc = r + delta[order][0], c + delta[order][1]
        if 0 <= nr < N and 0 <= nc < M:
            r, c = nr, nc
            h_top = (h_top + 3) % 4
            h_bottom = (h_top + 2) % 4
            if zido[r][c] != 0:
                hori[h_bottom] = zido[r][c]
                zido[r][c] = 0
            else:
                zido[r][c] = hori[h_bottom]
            vert[v_top] = hori[h_top]
            vert[v_bottom] = hori[h_bottom]
            print(hori[h_top])

    elif order == 2:
        nr, nc = r + delta[order][0], c + delta[order][1]
        if 0 <= nr < N and 0 <= nc < M:
            r, c = nr, nc
            h_top = (h_top + 1) % 4
            h_bottom = (h_top + 2) % 4
            if zido[r][c] != 0:
                hori[h_bottom] = zido[r][c]
                zido[r][c] = 0
            else:
                zido[r][c] = hori[h_bottom]
            vert[v_top] = hori[h_top]
            vert[v_bottom] = hori[h_bottom]
            print(hori[h_top])

    elif order == 3:
        nr, nc = r + delta[order][0], c + delta[order][1]
        if 0 <= nr < N and 0 <= nc < M:
            r, c = nr, nc
            v_top = (v_top + 1) % 4
            v_bottom = (v_top + 2) % 4
            if zido[r][c] != 0:
                vert[v_bottom] = zido[r][c]
                zido[r][c] = 0
            else:
                zido[r][c] = vert[v_bottom]
            hori[h_top] = vert[v_top]
            hori[h_bottom] = vert[v_bottom]
            print(hori[h_top])

    else:
        nr, nc = r + delta[order][0], c + delta[order][1]
        if 0 <= nr < N and 0 <= nc < M:
            r, c = nr, nc
            v_top = (v_top + 3) % 4
            v_bottom = (v_top + 2) % 4
            if zido[r][c] != 0:
                vert[v_bottom] = zido[r][c]
                zido[r][c] = 0
            else:
                zido[r][c] = vert[v_bottom]
            hori[h_top] = vert[v_top]
            hori[h_bottom] = vert[v_bottom]
            print(hori[h_top])
