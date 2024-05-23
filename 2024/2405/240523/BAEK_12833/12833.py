A, B, C = map(int, input().split())

count = C % 2
if count == 1:
    A = A ^ B

print(A)
