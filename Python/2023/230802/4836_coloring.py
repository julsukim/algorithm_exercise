T = int(input())
for tc in range(1, T+1):
    N = int(input())
    coloring = [list(map(int, input().split())) for _ in range(N)]

    colored_list = [['']*10 for _ in range(10)]
    colored = 0

    for k in range(N):
        si = coloring[k][0]
        sj = coloring[k][1]
        fi = coloring[k][2]
        fj = coloring[k][3]
        if coloring[k][4] == 1:
            for i in range(si, fi+1):
                for j in range(sj, fj+1):
                    colored_list[i][j] += 'r'
        else:
            for i in range(si, fi+1):
                for j in range(sj, fj+1):
                    colored_list[i][j] += 'b'

    for i in range(10):
        for element in colored_list[i]:
            if ('r' in element) and ('b' in element):
                colored += 1

    print(f'#{tc} {colored}')