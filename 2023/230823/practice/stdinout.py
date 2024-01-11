import sys
sys.stdin = open('input.txt', 'r')      # 'r' : 읽기전용으로 열기
# sys.stdout = open('output.txt', 'w')    # 파일에 출력 저장, 'w' : 쓰기전용으로 열기
# 1MB가 넘는 입력은 콘솔 버퍼에서 입력이 제대로 되지 않기 때문에 stdin 으로 입력이 필요


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(M+2)]+[[0] + list(map(int, input().split())) + [0] for _ in range(N)]+[[0]*(M+2)]

    print(arr)