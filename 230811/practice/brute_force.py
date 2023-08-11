sentence = 'Microscope'
word = 'scope'
N = len(sentence)
M = len(word)

result = 0
end = 0
for i in range(N - M + 1):
    for j in range(M):
        if sentence[i + j] != word[j]:
            break
    else:
        result = i
        end = i+M-1

print(result, end)
print(sentence[result:end+1])