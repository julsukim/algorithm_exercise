import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def recur(hint_idx, number):
    global answer
    if hint_idx == N:
        answer += 1
        recur(0, number+1)
        return

    # 1000 미만
    if number > 999:
        return

    # 중복 제거
    str_num = str(number)
    if str_num[0] == '0' or str_num[1] == '0' or str_num[2] == '0':
        recur(0, number+1)
        return
    if str_num[0] == str_num[1] or str_num[0] == str_num[2] or str_num[1] == str_num[2]:
        recur(0, number+1)
        return

    # 힌트 검사
    str_hint = str(hints[hint_idx][0])
    strike_cnt = 0
    ball_cnt = 0

    if str_num[0] == str_hint[0]:
        strike_cnt += 1
    elif str_num[0] == str_hint[1] or str_num[0] == str_hint[2]:
        ball_cnt += 1
    if str_num[1] == str_hint[1]:
        strike_cnt += 1
    elif str_num[1] == str_hint[0] or str_num[1] == str_hint[2]:
        ball_cnt += 1
    if str_num[2] == str_hint[2]:
        strike_cnt += 1
    elif str_num[2] == str_hint[0] or str_num[2] == str_hint[1]:
        ball_cnt += 1

    if strike_cnt == hints[hint_idx][1] and ball_cnt == hints[hint_idx][2]:
        # 힌트 통과
        recur(hint_idx+1, number)
    else:
        # 힌트 미통과
        recur(0, number+1)


N = int(input())
hints = [list(map(int, input().split())) for _ in range(N)]
answer = 0
recur(0, 100)
print(answer)
