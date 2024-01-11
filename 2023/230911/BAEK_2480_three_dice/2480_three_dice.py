D1, D2, D3 = map(int, input().split())

if D1 == D2 == D3:
    print(10000 + D1 * 1000)
elif D1 == D2:
    print(1000 + D1 * 100)
elif D1 == D3:
    print(1000 + D1 * 100)
elif D2 == D3:
    print(1000 + D2 * 100)
else:
    print(max(D1, D2, D3) * 100)
