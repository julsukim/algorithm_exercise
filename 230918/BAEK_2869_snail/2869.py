A, B, V = map(int, input().split())

# A*days - B*(days-1) >= V
# 단순히 반복문으로 일수를 구하면, 시간초과 발생.
# 일수를 주어진 조건으로 한번에 구하는 공식 만들기
days = (V-B)/(A-B)

# 일수가 정수가 아닐 수 있기 때문에 검사 후, 결과에 따라 출력
print(int(days) if days == int(days) else int(days)+1)
