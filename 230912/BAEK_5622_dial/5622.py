word = input()
total = 0
li2 = ['A', 'B', 'C']
li3 = ['D', 'E', 'F']
li4 = ['G', 'H', 'I']
li5 = ['J', 'K', 'L']
li6 = ['M', 'N', 'O']
li7 = ['P', 'Q', 'R', 'S']
li8 = ['T', 'U', 'V']
for chr in word:
    if chr in li2:
        total += 3
    elif chr in li3:
        total += 4
    elif chr in li4:
        total += 5
    elif chr in li5:
        total += 6
    elif chr in li6:
        total += 7
    elif chr in li7:
        total += 8
    elif chr in li8:
        total += 9
    else:
        total += 10
print(total)
