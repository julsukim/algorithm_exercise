T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    P = ''
    for chr in S:
        P += chr * R
    print(P)
