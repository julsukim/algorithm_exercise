def cantor(start, n):
    if n==0:
        return
    for i in range(start + (3**(n-1))*1, start + (3**(n-1))*2):
        str_list[i] = ' '
    cantor(start, n-1)
    cantor(start + (3**(n-1))*2, n-1)


while True:
    try:
        N = int(input())
        str_list = ['-']*(3**N)
        cantor(0, N)
        print(''.join(str_list))
    except:
        break
