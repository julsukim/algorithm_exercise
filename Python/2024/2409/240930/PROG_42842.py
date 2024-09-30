def solution(brown, yellow):
    # brown만 봤을 때, 최소 세로의 길이는 3이기 때문에 6을 뺀 나머지가 최대 가로 길이
    # 이때, 중간의 빈 공간의 면적을 계산해 가면서 yellow의 수와 맞을 때까지 세로길이를 늘이고(+2), 가로길이를 줄여보자(-2)
    # brown은 짝수로 주어질 수 밖에 없음
    width = (brown - 6)//2
    height = 3
    current_space = width * (height - 2)
    while current_space != yellow:
        width -= 1
        height += 1
        current_space = width * (height - 2)
    answer = [width + 2, height]
    return answer