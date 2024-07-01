import sys
sys.stdin = open('input.txt')


def enQ(value):
    global rear
    rear = (rear+1) % size
    cQ[rear] = value


def deQ():
    global front
    front = (front+1) % size
    return cQ[front]


def q_peek():
    return cQ[rear]


T = 10
for _ in range(1, T+1):
    tc = int(input())
    cQ = list(map(int, input().split()))
    cQ += [0]   # front의 자리는 공백이어야 하기 때문에 추가
    size = 9    # front 자리가 추가 되었기에 기존 8개의 숫자 + front 자리

    front = 8   # Queue에서 deQ한 값의 위치
    rear = 7    # Queue에서 가장 마지막에 들어간 값의 위치

    # Queue에서 값 하나를 deQ하고
    # 특정 숫자만큼 값을 뺀 후
    # - 뺀 값이 0보다 작으면 그대로 종료한다.
    # - 만약 음수라면 0으로 유지한다.
    # 다시 Queue에 enQ한다.
    dec_value = 1
    while q_peek() > 0:
        value = deQ() - dec_value
        enQ(value)

        dec_value += 1
        if dec_value >= 6:
            dec_value = 1
    cQ[rear] = 0

    print(f'#{tc}', end=' ')
    for _ in range(size-1):     # -1을 하는 이유는 front 위치는 출력 필요 없기 때문.
        print(deQ(), end=' ')
    print()
