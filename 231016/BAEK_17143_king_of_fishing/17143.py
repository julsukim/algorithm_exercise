# 격자판, 1~R, 1~C
R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
# row, column, 속력, 방향, 크기
# 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
fish_king = 0
tot = 0
while fish_king < (C+1):
    fish_king += 1
    mini = 101
    catch_list = []
    survived = []
    for shark in sharks:
        if shark[1] == fish_king:
            catch_list.append(shark)

    if len(catch_list) != 0:
        catch_list.sort()
        tot += catch_list[0][4]
        for shark in sharks:
            if shark != catch_list[0]:
                survived.append(shark)
    else:
        for shark in sharks:
            survived.append(shark)

    for shark in survived:
        if shark[2] == 0:
            continue
        pass

    sl = {}
    for shark in survived:
        try:
            sl[(shark[0], shark[1])].append(shark)
        except KeyError:
            sl[(shark[0], shark[1])] = [shark]

    sharks = []
    for l in sl:
        if len(sl[l]) >= 2:
            big_shark = 0
            largest = 0
            for i in range(len(sl[l])):
                if largest < sl[l][i][4]:
                    largest = sl[l][i][4]
                    big_shark = sl[l][i]
            else:
                sharks.append(big_shark)
        else:
            sharks.append(sl[l][0])

print(tot)
