A, B = map(int, input().split())
C = int(input())

CH = B + C
print((A + CH//60) % 24, CH % 60)
