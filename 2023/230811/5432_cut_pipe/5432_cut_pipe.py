'''
파이프 기준으로 보기 -> 레이저 기준으로 보기
레이저를 발사했을 때 잘라지는 개수는 현재의 파이프 수
괄호가 닫혔을 때 조각이 추가됨

현재 쌓인 막대 개수 cnt
총 조각수 ans
'('는 쇠막대 시작(or 레이저)
    cnt += 1

')' 레이저 s[i-1]=='('
        cnt -= 1
        ans += cnt
    or 쇠막대 끝


( 막대기 추가,
    cnt += 1
()레이저면,
    ans += cnt
) 막대기 끝이면,
    ans += 1
    cnt -= 1
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    pipes = input()
    N = len(pipes)

    cnt = 0
    ans = 0
    for i in range(N):
        if pipes[i] == '(':
            cnt += 1
        else:
            if pipes[i-1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1

    print(f'#{tc} {ans}')