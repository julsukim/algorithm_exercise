import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 참가 학생 수, 한 방에 배정가능한 최대 학생 수

    rooms = {}
    rooms[0] = [0]*7
    rooms[1] = [0]*7
    for _ in range(N):  # 방에 배정하기
        s, y = map(int, input().split())
        rooms[s][y] += 1

    room_count = 0
    for i in range(2):
        for j in range(1, 7):
            if rooms[i][j] != 0:
                room_count += (rooms[i][j] // K) + (rooms[i][j] % K > 0)

    print(room_count)
