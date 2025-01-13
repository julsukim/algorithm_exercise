from collections import deque

T = int(input())
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


def bfs(start, end):
    queue = deque([(start, 0)])
    visited = set(start)

    while queue:
        current, dist = queue.popleft()

        if current == end:
            return dist

        for nxt in keyboard[current]:
            if nxt not in visited:
                visited.add(nxt)

                queue.append((nxt, dist+2))

    return None


for _ in range(T):
    string = input()
    total = 0
    for i in range(1, len(string)):
        total += bfs(string[i-1], string[i])
    print(total + len(string))
