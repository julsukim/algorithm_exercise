# 14499 주사위 굴리기
# 동 1, 서 2, 북 3, 남 4
# 상단에 쓰여있는 값 출력
# 지도 바깥으로 이동 -> 명령 무시, 출력 X
N, M, r, c, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

# 주사위
#   2
# 4 1 3
#   5
#   6
dice = [0] * 7


# 주사위 굴리기
def roll_dice(direction):
    if direction == 1:  # 동쪽으로 굴리기
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 2:  # 서쪽으로 굴리기
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 3:  # 북쪽으로 굴리기
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    else:  # 남쪽으로 굴리기
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]


dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

for order in orders:
    nr = r + dr[order]
    nc = c + dc[order]

    # 지도 안에서만 이동
    if 0 <= nr < N and 0 <= nc < M:
        roll_dice(order)  # 주사위 굴리기

        # 주사위가 이동한 칸에 따라 바닥면, 지도의 값을 갱신
        if board[nr][nc] == 0:
            board[nr][nc] = dice[6]
        else:
            dice[6] = board[nr][nc]
            board[nr][nc] = 0

        print(dice[1])  # 상단 값 출력

        # 주사위 위치 갱신
        r, c = nr, nc
