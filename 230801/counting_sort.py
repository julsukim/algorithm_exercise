data = [8, 6, 3, 4, 5, 5, 2, 2, 9, 1]

max_d = data[0]
for i in data:
    if data[i] > max_d:
        max_d = data[i]
d_len = 0
for i in data:
    d_len += 1

counts = [0] * (max_d + 1)
temp = [0] * (d_len)

for i in range(0, d_len):
    counts[data[i]] += 1

print(counts)

for i in range(1, d_len):
    counts[i] += counts[i-1]

print(counts)

for i in range(d_len-1, -1, -1):
    counts[data[i]] -= 1
    temp[counts[data[i]]] = data[i]

print(temp)