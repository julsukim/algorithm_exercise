import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 학생 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 출발 방 번호는 홀수이고, 도착 방 번호는 짝수이다. 따라서 각각 200개의 방이 존재함.
    # 복도 번호를 공유하기 위해 조정이 필요 (예, 1번방과 2번방은 복도 공유)

    cnt = [0] * 201     # 방 사이의 공간을 지나는 사람 수 기록
    for a, b in arr:    # a<=b라는 보장이 없음
        # for i in range(a, b+1):
        a = (a+a%2)//2
        b = (b+b%2)//2
        for i in range(min(a, b), max(a, b)+1):
            cnt[i] += 1
    print(f'#{tc} {max(cnt)}')