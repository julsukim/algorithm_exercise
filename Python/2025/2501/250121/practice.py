# 변형 Z 탐색은, 기존의 좌상단 -> 우상단 -> 좌하단 -> 우하단 순서에서,
# 좌하단 -> 좌상단 -> 우상단 -> 우하단의 순서로 순회하며 번호를 매긴다.
# r, c의 방문 순서를 구하는 문제 (방문은 0부터 시작)

def modified_z(N, r, c):
    if N == 0:
        return 0

    half = 2 ** (N-1)
    total_elements = half * half

    # 2차원 배열을 4분할 하여 r, c이 위치한 사분면을 판별한다.
    # 좌하단
    if r >= half and c < half:
        return modified_z(N-1, r - half, c)
    # 좌상단
    elif r < half and c < half:
        return total_elements + modified_z(N-1, r, c)
    # 우상단
    elif r < half and c >= half:
        return 2 * total_elements + modified_z(N-1, r, c - half)
    elif r >= half and c >= half:
        return 3 * total_elements + modified_z(N-1, r - half, c - half)


N, r, c = map(int, input().split())
print(modified_z(N, r, c))
