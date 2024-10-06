import sys
input = sys.stdin.readline

words = input().rstrip()
M = int(input().rstrip())
arr = [list(input().rstrip().split()) for _ in range(M)]


def solution(string, m, queries):
    N = len(string)
    MAX = N + m + 2 # 최대 노드 수 (여유를 두기 위해 + 2)

    data = [''] * MAX # 각 노드의 문자를 저장
    prev = [-1] * MAX # 각 노드의 이전 노드의 인덱스를 저장
    next = [-1] * MAX # 각 노드의 다음 노드의 인덱스를 저장

    # 초기 연결 리스트 구성
    unused = N + 1  # 다음에 사용할 노드 인덱스
    for i in range(1, N + 1):
        data[i] = string[i - 1]
        prev[i] = i - 1
        next[i - 1] = i
    next[N] = -1  # 마지막 노드의 next는 -1
    prev[0] = -1  # 더미 노드의 prev는 -1

    cursor = N  # 커서를 문자열의 맨 뒤로 설정

    for query in queries:
        if query[0] == 'L':
            if prev[cursor] != -1:
                cursor = prev[cursor]
        elif query[0] == 'D':
            if next[cursor] != -1:
                cursor = next[cursor]
        elif query[0] == 'B':
            if cursor != 0:
                remove = cursor
                cursor = prev[cursor]
                if cursor != -1:
                    next[cursor] = next[remove]
                if next[remove] != -1:
                    prev[next[remove]] = cursor
        elif query[0] == 'P':
            c = query[1]
            data[unused] = c
            prev[unused] = cursor
            next[unused] = next[cursor]
            if next[cursor] != -1:
                prev[next[cursor]] = unused
            next[cursor] = unused
            cursor = unused
            unused += 1

    # 결과 문자열 생성
    result = []
    idx = next[0]
    while idx != -1:
        result.append(data[idx])
        idx = next[idx]

    return ''.join(result)


print(solution(words, M, arr))
