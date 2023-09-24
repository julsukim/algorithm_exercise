import sys
input = sys.stdin.readline


def recursion(S, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif S[l] != S[r]:
        return 0
    else:
        return recursion(S, l+1, r-1)


def is_palindrome(S):
    return recursion(S, 0, len(S)-1)


T = int(input())
for _ in range(T):
    S = input().strip()
    cnt = 0
    print(is_palindrome(S), cnt)
