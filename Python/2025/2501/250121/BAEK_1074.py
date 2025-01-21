# 2 ** N * 2 ** N인 2차원 배열을 Z 모양으로 탐색
def Z(N, r, c):
    # N=0이면 1×1 크기에서 멈추므로 방문 순서는 0.
    if N == 0:
        return 0

    # half = 2 ** (N-1) = (1 << (N-1))
    half = 2 ** (N - 1)
    size_per_quadrant = half * half  # 각 사분면이 갖는 원소(칸) 수

    # (r, c)가 어느 사분면인지 판별
    if r < half and c < half:
        # 왼쪽 위 사분면
        return Z(N - 1, r, c)
    elif r < half and c >= half:
        # 오른쪽 위 사분면
        return size_per_quadrant + Z(N - 1, r, c - half)
    elif r >= half and c < half:
        # 왼쪽 아래 사분면
        return 2 * size_per_quadrant + Z(N - 1, r - half, c)
    else:
        # 오른쪽 아래 사분면
        return 3 * size_per_quadrant + Z(N - 1, r - half, c - half)


# 입력 받기
N, r, c = map(int, input().split())

# 결과 출력
print(Z(N, r, c))
