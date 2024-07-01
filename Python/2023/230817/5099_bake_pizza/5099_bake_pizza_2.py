import sys
sys.stdin = open('input.txt')


def add_pizza(value):
    global front
    front = (front+1) % (N+1)
    fire_pot[front] = value


def take_out():
    global rear
    rear = (rear+1) % (N+1)
    return fire_pot[rear]


def is_full():
    return (rear+1) % (N+1) == front

def baking(N, M):
    done = []
    next_pizza = N

    for i in range(N):
        add_pizza(pizza[i])

    while len(done) < M:
        w = take_out()
        if (w[1] // 2) == 0:
            if next_pizza < M:
                add_pizza(pizza[next_pizza])
                next_pizza += 1
            done.append(w)
        else:
            w[1] = w[1] // 2
            add_pizza(w)

    return done[-1][0]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    pizza = []
    for key, value in enumerate(cheese):
        pizza.append([key+1, value])

    fire_pot = [0] * (N+1)
    front = 0
    rear = 0

    answer = baking(N, M)
    print(f'#{tc} {answer}')