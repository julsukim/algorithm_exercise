import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queries = [input().split() for _ in range(N)]
queue = deque()
printer = []
for query in queries:
    if query[0] == 'push':
        queue.append(query[1])

    elif query[0] == 'pop':
        if queue:
            printer.append(queue.popleft())
        else:
            printer.append('-1')

    elif query[0] == 'size':
        printer.append(str(len(queue)))

    elif query[0] == 'empty':
        if queue:
            printer.append('0')
        else:
            printer.append('1')

    elif query[0] == 'front':
        if queue:
            printer.append(queue[0])
        else:
            printer.append('-1')

    elif query[0] == 'back':
        if queue:
            printer.append(queue[-1])
        else:
            printer.append('-1')

print('\n'.join(printer))
