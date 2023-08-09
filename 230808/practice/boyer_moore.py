def pre_process(pattern, M): # M : 길이
    skip_dict = {}
    for i in range(M):
        if not skip_dict.get(pattern[M-i-1]):  # 중복된 값은 넣지 않음
            skip_dict[pattern[M-i-1]] = i

    return skip_dict


def boyer_moore(target, pattern, skip_dict):
    pat_len = len(pattern)
    p_idx = len(pattern) - 1  # 패턴의 마지막 부터 비교 시작
    i = 0  # 이동한 인덱스 위치 저장
    t_idx = i + p_idx   # 처음 비교위치는 동일함 why? 초기 비교기 때문!

    while t_idx <= len(target):
        # 패턴의 뒤에서 부터 확인
        if target[t_idx] == pattern[p_idx]: # 같다면
            t_idx -= 1
            p_idx -= 1

            if p_idx == -1:  # 다 찾았다면
                return t_idx + 1 # 다 찾고나서도 t_idx를 -1 했기 때문에 다시 +1

        else:  # 다르다면
            # skip 배열에 target과 일치하는 것이 존재하는지 확인
            if target[t_idx] in skip_dict.keys():  # 존재한다면
                p_idx = pat_len - 1   # p 인덱스는 마지막 패턴부터 비교하기에 마지막 인덱스에 위치
                i += skip_dict[target[i + p_idx]]  # 이동한 점을 기준으로 skip list 이동
                t_idx = i + p_idx                  # t_idx 를 바로 사용하지 않는 이유는 기준점(이전에 이동한 위치)에서 이동해야 하기 때문
            else:  # 존재하지 않는다면
                p_idx = pat_len - 1 # 가장 마지막 부분으로 이동 (뒤에서 부터 비교하기 때문에)
                i += pat_len          # 패턴의 길이만큼 더해서 그다음 마지막끼리 비교 하도록 변경
                t_idx = i + p_idx

    return -1




# target = "abcdabcdabcdabcef"
# target = 'a pattern matching algorithm'
target = 'baanaaabanaaaaana'
N = len(target)
# pattern = "abcdabcef"
# pattern = 'rithm'
pattern = 'bana'
M = len(pattern)
# Target 문자열의 길이

skip_dict = pre_process(pattern, M)
res = boyer_moore(target, pattern, skip_dict)
print(res)
