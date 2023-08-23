import sys
sys.stdin = open('input.txt')


def calc_tree(node):    # node : 정점 번호
    # 연산자라면 tree[node]의 길이가 4이고
    # 피연산자라면 tree[node]의 길이가 2이다.
    if len(tree[node]) == 2:
        return int(tree[node][1])
    else:   # 연산자라면,
        left = calc_tree(int(tree[node][2]))
        right = calc_tree(int(tree[node][3]))

        calc = {
            '+': left + right,
            '-': left - right,
            '*': left * right,
            # zero division 방지를 위한 조건 표현식
            # 조건 표현식이란?
            # (조건이 참인 경우 반환될 표현식) if 조건 else (조건이 거짓인 경우 반환될 표현식)
            '/': left // right if right else print('zero division')
        }
        return calc[tree[node][1]]


T = 10
for tc in range(1, T+1):
    N = int(input())    # 정점의 개수
    tree = [0] * (N+1)

    for idx in range(1, N+1):
        tree[idx] = input().split()

    result = calc_tree(1)
    print(f'#{tc} {result}')
