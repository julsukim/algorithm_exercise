import sys
input = sys.stdin.readline

M = int(input())
S = 0b000000000000000000000

for _ in range(M):
    order = list(input().split())
    if len(order) == 2:
        command, num = order[0], int(order[1])
        if command == "add":
            S = S | (0b1 << num)
        elif command == "remove":
            S = S & ~(0b1 << num)
        elif command == "check":
            if S & (0b1 << num):
                print(1)
            else:
                print(0)
        elif command == "toggle":
            S = S ^ (0b1 << num)
    else:
        command = order[0]
        if command == "all":
            S = 0b111111111111111111111
        elif command == "empty":
            S = 0b0
