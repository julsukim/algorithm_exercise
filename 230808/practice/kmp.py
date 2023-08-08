def makeLPS_v1(pattern):  # P는 패턴
    lp = len(pattern)
    LPS = [0] * lp  # 패턴의 길이와 같은크기의 테이블 생성 (longest proper prefix which is also suffix)
    s = 0  # s를 사용하여 테이블 값을 갱신한다
    for idx in range(1, lp):
        while s > 0 and pattern[s] != pattern[idx]:  # s와 idx가 다르면 s는 s-1의 테이블값 인덱스로 돌아간다
            s = LPS[s - 1]  # 왜?->현재의 s에서 idx와 다르니 s가 +1되었던것을 되돌아가서
            # s-1에서의 테이블값 인덱스에서 다시 idx와 비교해준다
            # 테이블에는 최대 공통 부분들이 있어서 돌아갈지점을 계속 갱신해주다가
            # 0까지 가면 0이 된다.0을 저장하고 다음 idx로 넘어간다

        if pattern[s] == pattern[idx]:  # 만약 같으면 s값을 1더해주고 LPS에 값을 넣는다.
            s += 1
            LPS[idx] = s

    return LPS


def makeLPS_v2(pattern):
    M = len(pattern)  # 패턴의 길이

    LPS = [0] * M # LPS 배열 생성
    same_p_idx = 0 # 동일 패턴 인덱스
    idx = 1 # 패턴체크 인덱스

    while idx < M: # M 길이 만큼 체크
        if pattern[same_p_idx] == pattern[idx]: # 같은 패턴을 가지고 있으면
            same_p_idx += 1 # 같은 패턴 발견해서 1 증가
            LPS[idx] = same_p_idx # 체크 인덱스 자리에 같은 패턴 갯수 추가
            idx += 1 # 다음 자리수 확인
        else:  # 패턴이 같지 않다면
            if same_p_idx != 0: # 현재 동일 패턴이 있으면
                # AAACAAAA 와 같은 패턴이 있는 경우
                # 마지막 AAAA 패턴에서 마지막 A는 4번째 자리인 C와 다름
                # 그래서 0으로 초기화 하려니 AAA 3개의 동일한 패턴을 가지고 있음
                # 해당 패턴인 경우라면 이전 same_p 값으로 돌아가서 (그럼 P[same_p] 는 A가 됨)
                # 현재 비교하려는 chk_idx와 비교하여 동일한 값이므로 패턴갯수가 유지됨
                same_p_idx = LPS[same_p_idx-1] # 이전 LPS 값으로
            else:
                LPS[idx] = 0
                idx += 1
    return LPS


def KMPSearch(P, T):
    M = len(P)
    N = len(T)

    LPS = makeLPS_v2(P)
    p_idx = 0
    t_idx = 0
    while t_idx < N:
        # 같은 글자면 다음 글자 확인
        if P[p_idx] == T[t_idx]:
            p_idx += 1
            t_idx += 1

            # 만약 다 찾은 경우 (인덱싱은 M-1 까지 이니 때문에 M과 같으면 다 검사한 것)
            if p_idx == M:
                return t_idx - p_idx

        else:  # 다른 글자인 경우
            if p_idx > 0:  # 패턴의 두 번째 글자 부터 틀린 경우
                p_idx = LPS[p_idx - 1]  # 패턴 인덱스 이동
            else:  # 앞글자 부터 틀리면 타겟의 다음 글자와 비교
                t_idx += 1

    return -1


# print(makeLPS_v1('abcdacba'))

# print(makeLPS_v1('abcdabcdaeabcf'))
# print(makeLPS_v2('abcdabcdaeabcf'))
# [0, 0, 0, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 0]
# [0, 0, 0, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 0]

# print(makeLPS_v1('AAACAAAAA'))
# print(makeLPS_v2('AAACAAAAA'))
#  [0, 1, 2, 0, 1, 2, 3, 3, 3]
#  [0, 1, 2, 0, 1, 2, 3, 3, 3]

# print(KMPSearch('aaacaaaaaaa', 'aaacaaaaaacaaaaaaaa')) # 7
# print(KMPSearch('ABCDABD', 'ABC ABCDAB ABCDABCDABDE')) # 15
