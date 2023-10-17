C = 4
arr = list(range(1, C+1)) + list(range(C-1, 0, -1))
m_arr = list(range(C, 1, -1)) + list(range(1, C+1))
print(arr, m_arr)
col = 2
speed = 2

print(arr[arr.index(col)+(speed%C)])
print(m_arr[(-1*m_arr.index(col)-1) - (speed%C)])
