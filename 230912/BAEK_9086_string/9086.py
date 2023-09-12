T = int(input())
for _ in range(1, T+1):
    word = input()
    N = len(word)
    print(word[0]+word[N-1])