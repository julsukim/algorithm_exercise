arr = [1, 2, 3]    # 부분 집합
selected = [False] * (len(arr) + 1)    # 해당 숫자의 선택 여부 확인 용도

def powerset(idx):    # idx 는 현재 숫자, 위치

    # 종료 조건 만들기
    if idx == len(arr)+1:    # +1 을 붙인 이유 => selected 크기가 len(arr) + 1 이기 때문
        # 종료 전에 현재 선택된 부분집합을 출력
        print(selected, end=': ')
        for i in range(len(arr) + 1):
            if selected[i] == True:
                print(i, end=' ')
        print()    # 줄 바꿈 용도
        return    # 함수 종료 (break 를 사용하듯이 함수를 종료하기 위한 목적)

    # 현 위치를 선택했을 경우
    selected[idx] = True
    powerset(idx+1)    # 다음 자리 선택

    # 현 위치를 선택하지 않았을 경우
    selected[idx] = False
    powerset(idx+1)    # 다음 자리 선택

powerset(1)    # 시작이 1인 이유 : 0번 index를 selected에서 사용하지 않기 때문