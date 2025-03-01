from collections import deque
import sys

input = sys.stdin.readline


def rotating_queue(N, M, targets):
    queue = deque(range(1, N + 1))
    total_operations = 0

    for target in targets:
        target_idx = queue.index(target)  # 현재 큐에서 목표 원소의 위치

        # 왼쪽 이동 vs 오른쪽 이동 최소값 선택
        left_moves = target_idx
        right_moves = len(queue) - target_idx
        min_moves = min(left_moves, right_moves)

        # 이동 수행
        if left_moves <= right_moves:
            queue.rotate(-left_moves)  # 왼쪽 이동
        else:
            queue.rotate(right_moves)  # 오른쪽 이동

        queue.popleft()  # 원소 제거
        total_operations += min_moves  # 최소 이동 횟수 추가

    return total_operations


# 입력 처리
N, M = map(int, input().split())
targets = list(map(int, input().split()))

# 결과 출력
print(rotating_queue(N, M, targets))
