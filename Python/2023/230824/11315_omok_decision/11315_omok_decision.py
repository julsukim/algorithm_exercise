import sys
sys.stdin = open('input.txt')


def omok_decision():
    result = 'NO'
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if omok[i][j] == 'o':
                    cnt = 1
                else:
                    cnt = 0
                for l in range(1, 5):
                    ni, nj = i + l * di[k], j + l * dj[k]
                    if 0<=ni<N and 0<=nj<N:
                        if omok[ni][nj] == 'o':
                            cnt += 1
                else:
                    if cnt >= 5:
                        result = 'YES'
                        return result

    return result


di = [0, -1, -1, -1]
dj = [1, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    omok = [input() for _ in range(N)]

    result = omok_decision()
    print(f'#{tc} {result}')