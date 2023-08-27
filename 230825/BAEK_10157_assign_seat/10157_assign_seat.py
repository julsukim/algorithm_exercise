import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    C, R = map(int, input().split())
    K = int(input())
    arr = [[0]*R for _ in range(C)]

    if C*R < K:
        print(0)
    else:
        dir = 0
        cnt = 0
        turn = 0
        find = False
        while cnt < C * R:
            if (dir % 4) == 0:
                turn += 1
                for i in range((turn - 1), C):
                    for j in range((turn - 1), R - (turn - 1)):
                        cnt += 1
                        if cnt == K:
                            print(i+1,j+1)
                            find = True
                            break
                        arr[i][j] = cnt
                    break
            elif (dir % 4) == 1:
                for j in range((R - 1 - (turn - 1)), -1, -1):
                    for i in range((turn), C - (turn - 1)):
                        cnt += 1
                        if cnt == K:
                            print(i+1,j+1)
                            find = True
                            break
                        arr[i][j] = cnt
                    break
            elif (dir % 4) == 2:
                for i in range((C - 1 - (turn - 1)), -1, -1):
                    for j in range((R - 1 - (turn)), (turn - 1) - 1, -1):
                        cnt += 1
                        if cnt == K:
                            print(i+1,j+1)
                            find = True
                            break
                        arr[i][j] = cnt
                    break
            else:
                for j in range((turn - 1), R):
                    for i in range((C - 1 - (turn)), turn - 1, -1):
                        cnt += 1
                        if cnt == K:
                            print(i+1,j+1)
                            find = True
                            break
                        arr[i][j] = cnt
                    break
            dir += 1
            if find:
                break
