import sys
sys.stdin = open('algo2_sample_in.txt')


def push(value):        # 카드덱 C에 카드 넣기
    global top
    top += 1
    card_stack[top] = value


def pop():              # 카드덱 C에서 카드 빼기
    global top
    top -= 1
    return card_stack[top + 1]


def enqueue(value):     # 카드덱 B에 카드 넣기
    global rear
    rear += 1
    card_queue[rear] = value


def dequeue():          # 카드덱 B에서 카드 빼기
    global front
    front += 1
    return card_queue[front]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cards = list(input().split())

    card_queue = [0] * (N * N)  # 카드덱 B
    front = -1
    rear = -1

    card_stack = [0] * (N*N)    # 카드덱 C
    top = -1

    bonus_num = 0               # 보너스 숫자
    for card in cards:          # 카드를 순서대로 가져오기
        if card == '+':
            bonus_num += 1      # '+'라면, 보너스 숫자 +1 하기
        else:
            num = int(card) + bonus_num
            if num % 2 == 1:    # 홀수라면 카드덱 B에 넣기
                enqueue(num)
            else:               # 짝수라면 카드덱 C에 넣기
                push(num)

    score = 0
    for i in range(1, N+1):     # 참가자에게 순서대로 카드 배분
        score_b = dequeue()     # 카드덱 B에서 점수 획득
        score_c = pop()         # 카드덱 C에서 점수 획득
        if i == M:              # 김싸피의 순서일 때 획득 점수
            score += score_b
            score += score_c

    print(f'#{tc} {score}')
