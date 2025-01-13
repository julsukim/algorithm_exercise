from collections import deque

# 키보드 인접 관계
keyboard = {
    'Q': ['W', 'A'],
    'W': ['Q', 'A', 'S', 'E'],
    'E': ['W', 'S', 'D', 'R'],
    'R': ['E', 'D', 'F', 'T'],
    'T': ['R', 'F', 'G', 'Y'],
    'Y': ['T', 'G', 'H', 'U'],
    'U': ['Y', 'H', 'J', 'I'],
    'I': ['U', 'J', 'K', 'O'],
    'O': ['I', 'K', 'L', 'P'],
    'P': ['O', 'L'],
    'A': ['Q', 'W', 'S', 'Z'],
    'S': ['A', 'W', 'E', 'D', 'X', 'Z'],
    'D': ['S', 'E', 'R', 'F', 'C', 'X'],
    'F': ['D', 'R', 'T', 'G', 'V', 'C'],
    'G': ['F', 'T', 'Y', 'H', 'B', 'V'],
    'H': ['G', 'Y', 'U', 'J', 'N', 'B'],
    'J': ['H', 'U', 'I', 'K', 'M', 'N'],
    'K': ['J', 'I', 'O', 'L', 'M'],
    'L': ['K', 'O', 'P'],
    'Z': ['A', 'S', 'X'],
    'X': ['Z', 'S', 'D', 'C'],
    'C': ['X', 'D', 'F', 'V'],
    'V': ['C', 'F', 'G', 'B'],
    'B': ['V', 'G', 'H', 'N'],
    'N': ['B', 'H', 'J', 'M'],
    'M': ['N', 'J', 'K'],
}

# 알파벳 목록 (문제에서 'A'~'Z'만 취급)
letters = list(keyboard.keys())  # 혹은 [chr(c) for c in range(ord('A'), ord('Z')+1)]


def build_dist_table():
    """
    26개 알파벳 각각에 대해 BFS를 한 번씩 수행하여
    dist[a][b] = a에서 b까지 이동하는 데 걸리는 최단 시간(초)을 구해둔다.
    """
    dist = {ch: {} for ch in letters}

    for start in letters:
        # BFS로 start -> 다른 문자까지의 최단 이동 시간 구하기
        queue = deque([(start, 0)])  # (현재 글자, 현재까지 이동 시간)
        visited = set([start])

        while queue:
            current, cost = queue.popleft()

            # dist[start][current] 저장
            dist[start][current] = cost

            # 인접 노드 탐색
            for nxt in keyboard[current]:
                if nxt not in visited:
                    visited.add(nxt)
                    # 한 간선 이동할 때마다 +2초
                    queue.append((nxt, cost + 2))

    return dist


def solve():
    # 1) dist 테이블 미리 계산 (알파벳 26개 x BFS)
    dist_table = build_dist_table()

    T = int(input().strip())
    for _ in range(T):
        s = input().strip()

        # 2) 문자열 입력 시간 = 누르는 시간(글자 수) + 이동 시간
        #    이동 시간은 dist_table[s[i-1]][s[i]] 이용
        time_move = 0
        for i in range(1, len(s)):
            time_move += dist_table[s[i - 1]][s[i]]

        # 버튼 누르는 시간 (각 글자마다 1초)
        time_press = len(s)

        # 총 시간
        total_time = time_move + time_press
        print(total_time)


solve()
