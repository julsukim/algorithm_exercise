str_list = 'JAEZNNZEAJ'
N = len(str_list)
M = 10
for i in range(N-M+1):
    for j in range(N-1, i, -1):
        if (str_list[i] == str_list[j]) and ((j-i) == M-1):
            sp = i
            ep = j
            for k in range(0, (j+i)//2 - 1):
                if str_list[i+k] != str_list[j-k]:
                    break
            else:
                for l in range(sp, ep+1):
                    print(f'{str_list[l]}', end='')
                print()