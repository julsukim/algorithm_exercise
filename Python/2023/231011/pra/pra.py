arr = list(range(1, 6))
N = len(arr)
R = 3
adj_arr = [0]*R
check = [0]*N


def comb(s, k, e):
    if s == e:
        print(adj_arr)
        return
    else:
        for i in range(k, N):
            adj_arr[s] = arr[i]
            comb(s+1, i+1, e)



def perm(s, e):
    if s == e:
        print(adj_arr)
        return
    else:
        for i in range(N):
            if check[i] == 0:
                check[i] = 1
                adj_arr[s] = arr[i]
                perm(s+1, e)
                check[i] = 0


comb(0, 0, R)
print('---')
perm(0, R)