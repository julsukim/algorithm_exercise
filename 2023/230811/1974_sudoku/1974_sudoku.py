'''
풀이 방법 :
1~9가 다 들어있는지? 확인하기
방법 1. 카운트 배열하기
방법 2. 한 행, 열 .. 을 중복제거하기 (ex. set)
    -> if 9개가 아니면, 겹치는 것이 있음!
'''
'''
i행, j열
ans = 1
for i : 0 -> 9
    tmp = set()
for j : 0 -> 9
    tmp = set()
3 x 3 영역 접근하기
왼쪽 위를 기준으로 범위 지정하기
for i : 0 -> 6, +3
    for j :
        i, j에 더해줄 것
        for p:
            for q:
'''
import sys
sys.stdin = open('input.txt')

def sudoku(arr, N):
    for i in range(N):
        cnt = [0]*(N+1)
        for j in range(N):
            cnt[arr[i][j]] += 1
        for k in range(1, N+1):
            if cnt[k] == 0:    # 1~9 사이에 빠진 숫자가 있으면
                return 0    # 0 리턴, 리턴 후에는 break 필요없음

    for j in range(N):
        cnt = [0]*(N+1)
        for k in range(N):
            cnt[arr[k][j]] += 1
        for l in range(1, N+1):
            if cnt[l] == 0:
                return 0

    for i in range(0, 6, 3):
        for j in range(0, 6, 3):
            cnt = [0]*(N+1)
            for p in range(0, 3):
                for q in range(0, 3):
                    cnt[arr[i+p][j+q]] += 1
            for k in range(1, N+1):
                if cnt[k] == 0:
                    return 0

    return 1


T = int(input())
for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = sudoku(arr, N)    # 스도쿠가 완성되면 1, 아니면 0
    print(f'#{tc} {ans}')
