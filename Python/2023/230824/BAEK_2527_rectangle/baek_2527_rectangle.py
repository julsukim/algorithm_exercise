import sys
sys.stdin = open('input.txt')

T = 4
for tc in range(1, T+1):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    result = ''
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        result = 'd'
    else:
        if (x1, y1) == (p2, q2) or (x1, q1) == (p2, y2) or (p1, y1) == (x2, q2) or (p1, q1) == (x2, y2):
            result = 'c'
        else:
            if x1 == p2 or p1 == x2 or y1 == q2 or q1 == y2:
                result = 'b'
            else:
                result = 'a'

    print(result)