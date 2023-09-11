H, M = map(int, input().split())

C = M - 45
if C < 0:
    if H == 0:
        print(23, 60 + C)
    else:
        print(H-1, 60 + C)
else:
    print(H, C)
