import sys
sys.stdin = open('input.txt', encoding='utf-8')

T = 10
for tc in range(1, T+1):
    M = int(input())  # M : 찾아야 하는 회문의 길이
    N = 8             # N : 배열의 크기 NxN
    arr = [input() for _ in range(N)]

    # 행 탐색은 행을 고정하고 열을 증가시켜서 확인
    # 열 탐색은 열을 고정하고 행을 증가시켜서 확인
    count = 0
    for line in range(N):
        for idx in range(N - M + 1):  # 반복필요횟수 = 총길이 - 뽑는문자길이 + 1
            row_str = ''
            col_str = ''
            # print(arr[line][idx])  # 행 탐색
            for delta in range(M):    # M개씩 문자를 뽑자
                row_str += arr[line][idx+delta]
                col_str += arr[idx+delta][line]
            # print(row_str, col_str)
            # 회문인지 확인
            # 체크 값 초기화
            row_palin = True
            col_palin = True
            for i in range(M // 2):
                if row_str[i] != row_str[M-1-i]:
                    row_palin = False
                if col_str[i] != col_str[M-1-i]:
                    col_palin = False
            # True + True => 2 형변환을 통해 정수의 합으로 바뀜
            count += row_palin + col_palin

    print(f'#{tc} {count}')