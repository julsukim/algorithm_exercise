A, B, V = map(int, input().split())

i = 1
while True:
    if V <= (A - B) * i + B:
        break
    i += 1

print(i)
