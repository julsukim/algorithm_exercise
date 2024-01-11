arr = ['a', 'b','c']
int_arr = [8, 3, 0, 4, 5, 7, 10, 2, 1, 2]
print(arr)
print(''.join(arr))
print('-'.join(arr))
print(' '.join(arr))
print('\n'.join(arr))
print(''.join(map(str, int_arr)))

for i in range(len(int_arr)):
    if i != 0 and i % 3 == 0:
        print()
    print(int_arr[i], end='.')