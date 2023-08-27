from pprint import pprint

N, M = 10, 15
arr = [[0]*M for _ in range(N)]
dir = 0
cnt = 0
turn = 0
while cnt < N*M:
    if (dir % 4) == 0:
        turn += 1
        for i in range((turn-1), N):
            for j in range((turn-1), M-(turn-1)):
                cnt += 1
                arr[i][j] = cnt
            break
    elif (dir % 4) == 1:
        for j in range((M-1-(turn-1)), -1, -1):
            for i in range((turn), N-(turn-1)):
                cnt += 1
                arr[i][j] = cnt
            break
    elif (dir % 4) == 2:
        for i in range((N-1-(turn-1)), -1, -1):
            for j in range((M-1-(turn)), (turn-1)-1, -1):
                cnt += 1
                arr[i][j] = cnt
            break
    else:
        for j in range((turn-1), M):
            for i in range((N-1-(turn)), turn-1, -1):
                cnt += 1
                arr[i][j] = cnt
            break
    dir += 1

pprint(arr)
