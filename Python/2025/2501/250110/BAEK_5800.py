K = int(input())
for i in range(1, K+1):
    arr = list(map(int, input().split()))

    scores = arr[1:]
    scores.sort(reverse=True)
    gaps = [scores[i] - scores[i+1] for i in range(0, arr[0] - 1)]

    print(f'Class {i}')
    print(f'Max {scores[0]}, Min {scores[-1]}, Largest gap {max(gaps)}')
