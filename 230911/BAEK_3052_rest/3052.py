B = 42
rest_list = []
for _ in range(10):
    A = int(input())
    rest_list.append(A%B)
set_list = set(rest_list)
print(len(set_list))
