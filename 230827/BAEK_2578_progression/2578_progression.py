import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    change = False # ascending / descending
    counting = 0
    stack = [0]
    top = -1
    for i in range(N):
        if len(stack) != 0:
            top += 1
            stack[top] = arr[i]
            counting += 1
        else:
            if change == False:
                if stack[top] >= arr[i]:
                    counting += 1
                else:
                    change = True
                    counting = 0