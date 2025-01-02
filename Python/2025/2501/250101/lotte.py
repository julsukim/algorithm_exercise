def count_possible_locations(n, m, star, observations):
    possible_count = 0  # 가능한 위치의 개수

    for p in range(1, n + 1):  # 별똥별의 추락 위치 p (세로)
        for q in range(1, m + 1):  # 별똥별의 추락 위치 q (가로)
            valid = True  # 해당 위치가 유효한지 확인
            for x, y, observed_brightness in observations:
                # 계산된 밝기
                calculated_brightness = max(star - (abs(p - x) + abs(q - y)), 0)
                # 관측된 밝기와 계산된 밝기가 다르면 유효하지 않음
                if calculated_brightness != observed_brightness:
                    valid = False
                    break
            if valid:
                possible_count += 1  # 유효한 위치이면 개수 증가

    return possible_count

# 테스트 데이터
n, m, star = 4, 4, 2
observations = [
    (3, 3, 0),  # 관측자 1: (x, y, 밝기)
    (4, 4, 0)
]

result = count_possible_locations(n, m, star, observations)
print(f"별똥별이 떨어질 수 있는 위치의 개수: {result}")
