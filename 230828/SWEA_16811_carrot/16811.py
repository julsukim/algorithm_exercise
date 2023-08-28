import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))

    min_ans = 1000
    for i in range(N-2):
        for j in range(i+1, N-1):
            if carrot[i]!=carrot[i+1] and carrot[j]!=carrot[j+1]:
                small = i+1
                mid = j-i
                large = N-1-j
                if small<=(N//2) and mid<=(N//2) and large<=(N//2):
                    if min_ans > (max(small, mid, large) - min(small, mid, large)):
                        min_ans = max(small, mid, large) - min(small, mid, large)
    if min_ans == 1000:
        min_ans = -1
    print(min_ans)
