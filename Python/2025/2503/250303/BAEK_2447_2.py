def make_pattern(n):
    # n이 1이면 기본 패턴 반환
    if n == 1:
        return ["*"]

    # n//3 크기의 패턴을 먼저 구한다.
    sub_pattern = make_pattern(n // 3)
    pattern = []

    # 윗부분: sub_pattern을 3번 이어붙임
    for line in sub_pattern:
        pattern.append(line * 3)

    # 중간 부분: 왼쪽과 오른쪽은 sub_pattern, 가운데는 공백으로 채움
    for line in sub_pattern:
        pattern.append(line + " " * (n // 3) + line)

    # 아랫부분: 윗부분과 동일하게 sub_pattern을 3번 이어붙임
    for line in sub_pattern:
        pattern.append(line * 3)

    return pattern


N = int(input())
result = make_pattern(N)
print("\n".join(result))
