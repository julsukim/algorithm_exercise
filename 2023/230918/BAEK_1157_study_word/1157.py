word = input().lower()

char_dict = {}
for i in word:
    if i in char_dict:
        char_dict[i] += 1
    else:
        char_dict[i] = 1

result = []
maximum = max(list(char_dict.values()))
for i in char_dict:
    if char_dict[i] == maximum:
        result.append(i)
if len(result) == 1:
    print(result[0].upper())
else:
    print('?')
