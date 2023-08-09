import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    word, sub_word = input().split()
    N = len(word)
    M = len(sub_word)

    count = 0
    i = 0
    while i < (N - M + 1):
        for j in range(M):
            if word[i + j] != sub_word[j]:
                break
        else:
            count += 1
            i += (M-1)
        i += 1
    type_count = N - ((M - 1) * count)

    print(f'#{tc} {type_count}')