def pre_process(pattern, M): # M : 길이
    skip_dict = {}
    for i in range(M):
        if not skip_dict.get(pattern[M-i-1]):  # 중복된 값은 넣지 않음
            skip_dict[pattern[M-i-1]] = i

    return skip_dict


def boyer_moore(target, pattern, skip_dict):
    p_idx = len(pattern) - 1  # 패턴의 마지막 부터 비교 시작
    t_idx = p_idx   # 처음 비교위치는 동일함 why? 첫 비교이기 때문!

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
                t_idx += skip_dict[target[t_idx]]  # 패턴의 마지막과 비교할 곳
                p_idx = len(pattern) - 1   # p 인덱스는 마지막 패턴부터 비교하기에 마지막 인덱스에 위치
            else:  # 존재하지 않는다면
                t_idx += len(pattern) # 패턴의 길이만큼 더해서 그다음 마지막끼리 비교 하도록 변경
                p_idx = len(pattern) - 1 # 가장 마지막 부분으로 이동 (뒤에서 부터 비교하기 때문에)

    return -1




# target = "abcdabcdabcdabcef"
target = 'a pattern matching algorithm'
N = len(target)
# pattern = "abcdabcef"
pattern = 'rithm'
M = len(pattern)
# Target 문자열의 길이

skip_dict = pre_process(pattern, M)
res = boyer_moore(target, pattern, skip_dict)
print(res)
