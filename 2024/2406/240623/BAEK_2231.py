def finder(t):
    ans = int(t)
    # for c in t:
    #     ans += int(c)
    ans += sum(map(int, t))
    if ans == N:
        return True


N = int(input())

tmp = 1
flag = False
while tmp < N:
    if finder(str(tmp)):
        print(tmp)
        flag = True
        break
    tmp += 1
if not flag:
    print(0)
