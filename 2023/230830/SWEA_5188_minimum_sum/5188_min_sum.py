import sys
sys.stdin = open('input.txt')


def movemove(i, j, goal, s):
    global min_sum
    if min_sum < s:
        return
    elif i+1>N or j+1>N:
        return
    elif (i, j) == goal:
        s += arr[i][j]
        if min_sum > s:
            min_sum = s
        return
    else:
        movemove(i+1, j, goal, s+arr[i][j])
        movemove(i, j+1, goal, s+arr[i][j])
        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 300

    movemove(0, 0, (N-1, N-1), 0)
    print(f'#{tc} {min_sum}')