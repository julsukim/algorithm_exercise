import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    num = N
    i = 1
    converted = ''
    print(f'#{tc}', end=' ')
    while num != 0:
        converted += str(int(num // 2**(-i)))
        num = num % 2**(-i)
        i += 1
        if i > 13:
            print('overflow')
            break
    else:
        print(converted)