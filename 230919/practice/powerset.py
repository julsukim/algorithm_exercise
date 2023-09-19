# {1, 2, 3} 집합에서 3개의 숫자를 선택하는 기본적인 예제


arr = [i for i in range(1, 4)]
path = [0] * 3


def backtracking(cnt):
    # 기저 조건
    # 숫자 3개를 골랐을 때 종료
    if cnt == 3:
        print(*path)
        return

    for num in arr:
        # 들어가기 로직 - 경로 저장
        path[cnt] = num
        # 다음 재귀 함수 호출
        backtracking(cnt + 1)
        # 돌아와서 할 로직


backtracking(0)
