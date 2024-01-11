def f(i, N, K):     # i 이전에 고른 개수, N 개에서 K개를 골라 만드는 순열
    if i == K:      # 순열 완성: K개를 모두 고른 경우
        print(p)
        return
    else:   # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:    # 아직 사용되기 전이면,
                p[i] = numbers[j]
                used[j] = 1
                f(i+1, N, K)
                used[j] = 0


numbers = [1, 2, 3, 4, 5]
N = 5   # N개의 숫자에서
K = 3   # K개를 골라 만드는 순열
used = [0] * N  # 이미 사용한 카드인지 표시
p = [0] * K
f(0, N, K)
