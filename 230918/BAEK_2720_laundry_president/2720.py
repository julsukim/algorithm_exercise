T = int(input())
for _ in range(T):
    C = int(input())
    result = [0]*4
    result[0] = C//25
    C = C%25
    result[1] = C//10
    C = C%10
    result[2] = C//5
    C = C%5
    result[3] = C//1
    C = C%1
    print(*result)
