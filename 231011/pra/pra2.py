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


# comb(0, 0, R)
# perm(0, R)

# 기본
# for i in range(1<<N):
#     subset = []
#     for j in range(N):
#         if i&(1<<j):
#             subset.append(arr[j])
#     print(subset)

# 공집합, 최초 리스트 제외
# for i in range(1, (1<<N)-1):
#     subset = []
#     for j in range(N):
#         if i&(1<<j):
#             subset.append(arr[j])
#     print(subset)

# subset 2개 만들기
# for i in range(1, (1<<N)-1):
#     subset1 = []
#     subset2 = []
#     for j in range(N):
#         if i&(1<<j):
#             subset1.append(arr[j])
#         else:
#             subset2.append(arr[j])
#     print(subset1, subset2)

# 중복을 제거한 subsets
for i in range(1, (1<<N)//2):
    subset1 = []
    subset2 = []
    for j in range(N):
        if i&(1<<j):
            subset1.append(arr[j])
        else:
            subset2.append(arr[j])
    print(subset1, subset2)





















