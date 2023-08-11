import sys
sys.stdin = open('input.txt')

def rotateArray(arr, N):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][(N-1)-i] = arr[i][j]
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_arr = [list(map(int, input().split())) for _ in range(N)]

    ans_90 = rotateArray(num_arr, N)
    ans_180 = rotateArray(ans_90, N)
    ans_270 = rotateArray(ans_180, N)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, ans_90[i])), end=' ')
        print(''.join(map(str, ans_180[i])), end=' ')
        print(''.join(map(str, ans_270[i])), end=' ')
        print()
