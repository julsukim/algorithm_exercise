from collections import Counter

string = "Hello World!"
count = Counter(char.lower() for char in string if char.isalpha())
print(count)
