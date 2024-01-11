import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    brakets =input()
    br_dict = {'(': ')', '{': '}', '[': ']'}
    open_br = ['(', '{', '[']
    close_br = [')', '}', ']']
    arr = []

    print(f'#{tc}', end=' ')
    for i in brakets:
        if i in open_br:
            arr.append(i)
        elif i in close_br:
            if len(arr) == 0:
                print(-1)
                break
            elif br_dict[arr[-1]] == i:
                arr.pop()
            else:
                print(-1)
                break
    else:
        if len(arr) == 0:
            print(1)
        else:
            print(-1)