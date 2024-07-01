N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

answers = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            tmp = 0
            for cur in times:
                num = str(cur[0])
                strike = 0
                ball = 0
                if int(num[0]) == i:
                    strike += 1
                elif int(num[0]) == j:
                    ball += 1
                elif int(num[0]) == k:
                    ball += 1
                if int(num[1]) == j:
                    strike += 1
                elif int(num[1]) == i:
                    ball += 1
                elif int(num[1]) == k:
                    ball += 1
                if int(num[2]) == k:
                    strike += 1
                elif int(num[2]) == i:
                    ball += 1
                elif int(num[2]) == j:
                    ball += 1
                if strike == cur[1] and ball == cur[2]:
                    tmp += 1
            if tmp == N:
                answers += 1

print(answers)
