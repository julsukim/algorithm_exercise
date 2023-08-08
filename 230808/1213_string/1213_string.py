import sys
sys.stdin = open('input.txt', encoding='UTF8')

T = 10
for tc in range(1, T+1):
    TC = int(input())
    word = input()
    M = len(word)
    sentence = input()
    N = len(sentence)

    count = 0
    for i in range(N-M+1):
        for j in range(M):
            if sentence[i+j] != word[j]:
                break
        else:
            count += 1

    print(f'#{TC} {count}')