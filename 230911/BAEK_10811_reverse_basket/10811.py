N, M = map(int, input().split())
b_list = list(range(N+1))
for _ in range(M):
    ch = list(map(int, input().split()))
    ch.sort()
    cnt = 0
    if ch[0] == ch[1]:
        pass
    else:
        while cnt <= (ch[1]-ch[0])//2:
            b_list[ch[0]+cnt], b_list[ch[1]-cnt] = b_list[ch[1]-cnt], b_list[ch[0]+cnt]
            cnt += 1
for i in range(1, N+1):
    print(b_list[i], end=' ')
